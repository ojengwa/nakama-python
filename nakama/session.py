import re
import json
import base64
import time


JWT_REG = re.compile('^([A-Za-z0-9-_=]+)\.([A-Za-z0-9-_=]+)\.?([A-Za-z0-9-_.+/=]*)$')


class Session():

    @property
    def expired(self):
        return time.time() > self.expires

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self.set_token(token)

    @property
    def auth_header(self):
        return self._auth_header

    def __init__(self, client, server_key):
        self.client = client
        self.set_basic(server_key)

    def set_token(self, token):
        p1, p2, p3 = JWT_REG.match(token).groups()
        assert p1 and p2 and p3, 'JWT is not valid'

        p2 = p2.encode()
        pad = len(p2) % 4
        p2 += b"="*pad  # correct padding
        decoded_token = json.loads(base64.b64decode(p2))

        self._token = token
        self.expires = decoded_token['exp']
        self.username = decoded_token['usn']
        self.user_id = decoded_token['uid']
        self.vars = decoded_token.get('vrs')

        self._auth_header = {
            'Authorization': 'Bearer %s' % token
        }

    def set_refresh_token(self, refresh_token):
        self.refresh_token = refresh_token

    def set_basic(self, server_key):
        self._token = None
        self.refresh_token = None
        self.expires = None
        self.username = None
        self.user_id = None
        self.vars = None

        server_key = '%s:' % server_key

        self._auth_header = {
            'Authorization': 'Basic %s' % base64.b64encode(server_key.encode()).decode()
        }

    async def refresh(self, vars=None):
        assert self.refresh_token is not None, 'You must specify refresh token'

        body = {
            'token': self.refresh_token
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/session/refresh'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            # TO DO: update session
            return await resp.json()

    async def logout(self):
        assert self.token is not None, 'You must specify token'

        body = {
            'token': self.token
        }
        if self.refresh_token is not None:
            body['refreshToken'] = self.refresh_token

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/session/logout'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            # TO DO: update session
            return await resp.json()
