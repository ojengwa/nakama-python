class Purchase():

    def __init__(self, client):
        self.client = client

    async def validate_apple(self, receipt):
        body = {
            'receipt': receipt
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/iap/purchase/apple'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def validate_google(self, purchase):
        body = {
            'purchase': purchase
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/iap/purchase/google'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()

    async def validate_huawei(self, purchase, signature):
        body = {
            'purchase': purchase,
            'signature': signature
        }

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/iap/purchase/huawei'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()
