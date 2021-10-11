class Channel():

    def __init__(self, client):
        self.client = client

    async def get_history(self, channel_id, forward=None,
                          limit=None, cursor=None):
        params = {
            'channel_id': channel_id
        }
        if forward is not None:
            params['forward'] = forward and 'true' or 'false'
        if limit is not None:
            assert 1 <= limit <= 100, 'Limit must be between 1 and 100'
            params['limit'] = limit
        if cursor is not None:
            params['cursor'] = cursor

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/channel'
        async with self.client._http_session.get(url_path, params=params,
                                                  headers=headers) as resp:
            return await resp.json()
