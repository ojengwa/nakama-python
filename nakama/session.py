import re
import json
import base64


JWT_REG = re.compile('^(.-)%.(.-)%.(.-)$')


class Session():

    @property
    def expired(self):
        pass

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
        p1, p2, p3 = JWT_REG.match(token)
        assert p1 and p2 and p3, 'JWT is not valid'
        decoded_token = json.loads(base64.b64decode(p2))

        self._token = token
        self.expires = decoded_token['exp']
        self.username = decoded_token['usn']
        self.user_id = decoded_token['uid']
        self.vars = decoded_token['vrs']

        self._auth_header = {
            'Authorization': 'Bearer %s' % token
        }

    def set_basic(self, server_key):
        self._token = None
        self.expires = None
        self.username = None
        self.user_id = None
        self.vars = None

        server_key = '%s:' % server_key

        self._auth_header = {
            'Authorization': 'Basic %s' % base64.b64encode(server_key.encode()).decode()
        }

    async def refresh(self):
        pass

    async def logout(self):
        pass
