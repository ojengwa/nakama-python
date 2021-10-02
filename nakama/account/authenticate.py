class Authenticate():
    # TO DO:
    # update session when auth

    def __init__(self, client):
        self.client = client

    async def email(self, email, password,
                    vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'email': email,
            'password': password
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/email'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def device(self, id, vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'id': id
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/device'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def custom(self, id, vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'id': id
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/custom'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def apple(self, token, vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'token': token
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/apple'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def facebook(self, token, vars=None,
                       create=None, username=None, import_friends=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username
        if import_friends is not None:
            params['import'] = import_friends and 'true' or 'false'

        body = {
            'token': token
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/facebook'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def facebook_instant_game(self, signed_player_info,
                                    vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'signedPlayerInfo': signed_player_info
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/facebookinstantgame'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def game_center(self, bundle_id, player_id, public_key_url, salt,
                          signature, timestamp,
                          vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'bundleId': bundle_id,
            'playerId': player_id,
            'publicKeyUrl': public_key_url,
            'salt': salt,
            'signature': signature,
            'timestampSeconds': timestamp
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/gamecenter'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def google(self, token, vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'token': token
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/google'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def steam(self, token, vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create and 'true' or 'false'
        if username is not None:
            params['username'] = username

        body = {
            'token': token
        }
        if vars is not None:
            body['vars'] = vars

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/authenticate/google'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()
