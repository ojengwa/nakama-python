class Leaderboard():

    def __init__(self, client):
        self.client = client

    async def get_records(self, leaderboard_id, owner_ids=None,
                          limit=None, expiry=None, cursor=None):
        params = {}
        if owner_ids is not None:
            params['owner_ids'] = owner_ids
        if limit is not None:
            params['limit'] = limit
        if expiry is not None:
            params['expiry'] = expiry
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/leaderboard/%s' % leaderboard_id)
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()

    async def add_record(self, leaderboard_id, score, subscore=None,
                         operator=None, metadata=None):
        body = {
            'score': score
        }
        if subscore is not None:
            body['subscore'] = subscore
        if operator is not None:
            body['operator'] = operator
        if metadata is not None:
            body['metadata'] = metadata

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/leaderboard/%s' % leaderboard_id)
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def delete_record(self, leaderboard_id):
        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/leaderboard/%s' % leaderboard_id)
        async with self.client._http_session.delete(url_path,
                                                    headers=headers) as resp:
            return await resp.json()

    async def get_user_records(self, leaderboard_id, owner_id,
                               limit=None, expiry=None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if expiry is not None:
            params['expiry'] = expiry

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/leaderboard/%s/owner/%s' %
                                            (leaderboard_id, owner_id))
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()
