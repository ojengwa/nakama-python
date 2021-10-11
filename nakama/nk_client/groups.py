class Groups():

    def __init__(self, client):
        self.client = client

    async def create(self, name, description=None, max_member_count=None,
                     is_open=None, lang_tag=None, avatar_url=None):
        body = {
            'name': name
        }
        if description is not None:
            body['description'] = description
        if max_member_count is not None:
            body['maxCount'] = max_member_count
        if is_open is not None:
            body['open'] = is_open
        if lang_tag is not None:
            body['langTag'] = lang_tag
        if avatar_url is not None:
            body['avatarUrl'] = avatar_url

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/group'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def list(self, search_str=None, limit=None, cursor=None):
        params = {}
        if search_str is not None:
            params['name'] = search_str
        if limit is not None:
            params['limit'] = limit
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/group'
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()

    async def delete(self, group_id):
        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s' % group_id)
        async with self.client._http_session.delete(url_path,
                                                    headers=headers) as resp:
            return await resp.json()

    async def update(self, group_id, name=None, description=None,
                     max_member_count=None, is_open=None,
                     lang_tag=None, avatar_url=None):
        body = {}
        if name is not None:
            body['name'] = name
        if description is not None:
            body['description'] = description
        if max_member_count is not None:
            body['maxCount'] = max_member_count
        if is_open is not None:
            body['open'] = is_open
        if lang_tag is not None:
            body['langTag'] = lang_tag
        if avatar_url is not None:
            body['avatarUrl'] = avatar_url

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s' % group_id)
        async with self.client._http_session.put(url_path,
                                                 headers=headers,
                                                 json=body) as resp:
            return await resp.json()

    async def add_user(self, group_id, user_ids):
        params = {
            'user_ids': user_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/add' % group_id)
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()

    async def join(self, group_id):
        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/join' % group_id)
        async with self.client._http_session.post(url_path,
                                                  headers=headers) as resp:
            return await resp.json()

    async def leave(self, group_id):
        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/leave' % group_id)
        async with self.client._http_session.post(url_path,
                                                  headers=headers) as resp:
            return await resp.json()

    async def kick_user(self, group_id, user_ids):
        params = {
            'user_ids': user_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/kick' % group_id)
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()

    async def ban_user(self, group_id, user_ids):
        params = {
            'user_ids': user_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/ban' % group_id)
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()

    async def promote_user(self, group_id, user_ids):
        params = {
            'user_ids': user_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/promote' % group_id)
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()

    async def demote_user(self, group_id, user_ids):
        params = {
            'user_ids': user_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/demote' % group_id)
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()

    async def get_users(self, group_id, limit=None, state=None, cursor=None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if state is not None:
            params['state'] = state
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/group/%s/user' % group_id)
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()
