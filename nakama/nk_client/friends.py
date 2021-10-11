class Friends():

    def __init__(self, client):
        self.client = client

    async def list(self, limit=None, state=None, cursor=None):
        params = {}
        if limit is not None:
            params['create'] = limit
        if state is not None:
            params['username'] = state
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/friend'
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()

    async def add(self, user_ids=None, usernames=None):
        params = {}
        if user_ids is not None:
            params['ids'] = user_ids
        if usernames is not None:
            params['usernames'] = usernames

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/friend'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()

    async def delete(self, user_ids=None, usernames=None):
        params = {}
        if user_ids is not None:
            params['ids'] = user_ids
        if usernames is not None:
            params['usernames'] = usernames

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/friend'
        async with self.client._http_session.delete(url_path, params=params,
                                                    headers=headers) as resp:
            return await resp.json()

    async def block(self, user_ids=None, usernames=None):
        params = {}
        if user_ids is not None:
            params['ids'] = user_ids
        if usernames is not None:
            params['usernames'] = usernames

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/friend/block'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()

    async def import_facebook(self, fb_token, reset_friends=None):
        params = {}
        if reset_friends is not None:
            params['reset'] = reset_friends and 'true' or 'false'

        body = {
            'token': fb_token
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/friend/facebook'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def import_steam(self, stm_token, reset_friends=None):
        params = {}
        if reset_friends is not None:
            params['reset'] = reset_friends and 'true' or 'false'

        body = {
            'token': stm_token
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/friend/steam'
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()
