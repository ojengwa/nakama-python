class Storage():

    def __init__(self, client):
        self.client = client

    async def read(self, object_ids):
        body = {
            'objectIds': object_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/storage'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def write(self, objects):
        body = {
            'objects': objects
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/storage'
        async with self.client._http_session.put(url_path,
                                                 headers=headers,
                                                 json=body) as resp:
            return await resp.json()

    async def delete(self, object_ids):
        body = {
            'objectIds': object_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/storage/delete'
        async with self.client._http_session.put(url_path,
                                                 headers=headers,
                                                 json=body) as resp:
            return await resp.json()

    async def list(self, collection, user_id=None, limit=None, cursor=None):
        params = {
            'user_id': user_id or 'null'
        }
        if limit is not None:
            params['limit'] = limit
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + ('/v2/storage/%s' % collection)
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()
