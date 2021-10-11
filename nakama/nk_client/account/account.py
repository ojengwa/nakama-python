from .authenticate import Authenticate
from .link import Link
from .unlink import Unlink


class Account():

    def __init__(self, client):
        self.client = client

        self._authenticate = Authenticate(client)
        self._link = Link(client)
        self._unlink = Unlink(client)

    async def get(self):
        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account'
        async with self.client._http_session.get(url_path,
                                                 headers=headers) as resp:
            return await resp.json()

    async def update(self, **kwargs):
        body = {}
        if 'avatar_url' in kwargs.keys():
            body['avatarUrl'] = kwargs['avatar_url']
        if 'display_name' in kwargs.keys():
            body['displayName'] = kwargs['display_name']
        if 'lang_tag' in kwargs.keys():
            body['langTag'] = kwargs['lang_tag']
        if 'location' in kwargs.keys():
            body['location'] = kwargs['location']
        if 'timezone' in kwargs.keys():
            body['timezone'] = kwargs['timezone']
        if 'username' in kwargs.keys():
            body['username'] = kwargs['username']

        headers = self.client.session.auth_header

        url_path = self.client._http_uri + '/v2/account'
        async with self.client._http_session.put(url_path,
                                                 headers=headers,
                                                 json=body) as resp:
            return await resp.json()

    @property
    def authenticate(self):
        return self._authenticate

    @property
    def link(self):
        return self._link

    @property
    def unlink(self):
        return self._unlink
