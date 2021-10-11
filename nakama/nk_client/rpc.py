class RPC():

    def __init__(self, client):
        self.client = client

    async def __call__(self, func_id, http_key=None, **kwargs):
        params = {}
        headers = self.client.session.auth_header
        if http_key is not None:
            params['http_key'] = http_key
            headers = None

        url_path = self.client._http_uri + ('/v2/rpc/%s' % func_id)
        async with self.client._http_session.post(url_path, params=params,
                                                  headers=headers,
                                                  json=kwargs) as resp:
            return await resp.json()

    def __getattr__(self, name):
        def rpc_func(self, http_key=None, **kwargs):
            return self.__call__(name, http_key=http_key, **kwargs)
        return rpc_func
