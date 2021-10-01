class Unlink():

    def __init__(self, client):
        self.client = client

    async def email(self, email, password):
        body = {
            'email': email,
            'password': password
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/email'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def device(self, id):
        body = {
            'id': id
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/device'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def custom(self, id):
        body = {
            'id': id
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/custom'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def apple(self, token):
        body = {
            'token': token
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/apple'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def facebook(self, token):
        body = {
            'token': token
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/facebook'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def facebook_instant_game(self, signed_player_info):
        body = {
            'signedPlayerInfo': signed_player_info
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/facebookinstantgame'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def game_center(self, bundle_id, player_id, public_key_url, salt,
                          signature, timestamp):
        body = {
            'bundleId': bundle_id,
            'playerId': player_id,
            'publicKeyUrl': public_key_url,
            'salt': salt,
            'signature': signature,
            'timestampSeconds': timestamp
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/gamecenter'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def google(self, token):
        body = {
            'token': token
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/google'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def steam(self, token):
        body = {
            'token': token
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account/unlink/google'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()
