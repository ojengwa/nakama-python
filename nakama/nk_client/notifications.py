class Notifications():

    def __init__(self, client):
        self.client = client

    async def get(self, limit=None, cursor=None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/notification'
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()

    async def delete(self, notification_ids):
        params = {
            'ids': notification_ids
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/notification'
        async with self.client._http_session.delete(url_path, params=params,
                                                    headers=headers) as resp:
            return await resp.json()
