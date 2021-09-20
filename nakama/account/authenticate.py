class Authenticate():

    def __init__(self, client):
        self.client = client

    async def email(self):
        pass

    async def device(self):
        pass

    async def custom(self, id, vars=None, create=None, username=None):
        params = {}
        if create is not None:
            params['create'] = create
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

    async def apple(self):
        pass

    async def facebook(self):
        pass

    async def facebook_instant_game(self):
        pass

    async def game_center(self):
        pass

    async def google(self):
        pass

    async def steam(self):
        pass
