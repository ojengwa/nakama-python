class Users():

    def __init__(self, client):
        self.client = client

    async def get(self, ids=None, usernames=None, facebook_ids=None):
        params = {}
        if ids is not None:
            params['ids'] = ids
        if usernames is not None:
            params['usernames'] = usernames
        if facebook_ids is not None:
            params['facebook_ids'] = facebook_ids

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/user'
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()

    async def get_user_groups(self, user_id, limit=None,
                              state=None, cursor=None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if state is not None:
            params['state'] = state
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/user/%s/group' % user_id)
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()
