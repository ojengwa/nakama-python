class Tournaments():

    def __init__(self, client):
        self.client = client

    async def list(self, category_start=None, category_end=None,
                   start_time=None, end_time=None, limit=None, cursor=None):
        params = {}
        if category_start is not None:
            params['category_start'] = category_start
        if category_end is not None:
            params['category_end'] = category_end
        if start_time is not None:
            params['start_time'] = start_time
        if end_time is not None:
            params['end_time'] = end_time
        if limit is not None:
            params['limit'] = limit
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/tournament'
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()

    async def get_records(self, tournament_id, owner_ids=None,
                          limit=None, cursor=None):
        params = {}
        if owner_ids is not None:
            params['owner_ids'] = owner_ids
        if limit is not None:
            params['limit'] = limit
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/tournament/%s' % tournament_id)
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()

    async def add_record(self, tournament_id, score, subscore=None,
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

        url_path = self.client._http_uri + ('/v2/tournament/%s' % tournament_id)
        async with self.client._http_session.put(url_path,
                                                 headers=headers,
                                                 json=body) as resp:
            return await resp.json()

    async def join(self, tournament_id):
        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/tournament/%s/join' % tournament_id)
        async with self.client._http_session.post(url_path,
                                                  headers=headers) as resp:
            return await resp.json()

    async def get_user_records(self, tournament_id, owner_id,
                               limit=None, expiry=None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if expiry is not None:
            params['expiry'] = expiry

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/tournament/%s/owner/%s' %
                                            (tournament_id, owner_id))
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()
