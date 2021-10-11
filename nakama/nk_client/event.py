class Event():

    def __init__(self, client):
        self.client = client

    async def send(self, name, properties, external=None, timestamp=None):
        body = {
            'name': name,
            'properties': properties
        }
        if external is not None:
            body['external'] = external
        if timestamp is not None:
            body['timestamp'] = timestamp

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/event'
        async with self.client._http_session.post(url_path,
                                                  headers=headers,
                                                  json=body) as resp:
            return await resp.json()
