class Matches():

    def __init__(self, client):
        self.client = client

    async def list(self, limit=None, is_authoritative=None, label=None,
                   min_size=None, max_size=None, query=None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if is_authoritative is not None:
            params['authoritative'] = is_authoritative and 'true' or 'false'
        if label is not None:
            params['label'] = label
        if min_size is not None:
            params['min_size'] = min_size
        if max_size is not None:
            params['max_size'] = max_size
        if query is not None:
            params['query'] = query

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/match'
        async with self.client._http_session.get(url_path, params=params,
                                                 headers=headers) as resp:
            return await resp.json()
