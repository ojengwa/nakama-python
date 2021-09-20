from nakama.account.authenticate import Authenticate
from nakama.account.link import Link
from nakama.account.unlink import Unlink


class Account():

    def __init__(self, client):
        self.client = client

        self._authenticate = Authenticate(client)
        self._link = Link(client)
        self._unlink = Unlink(client)

    async def get(self):
        pass

    async def update(self):
        pass

    @property
    def authenticate(self):
        return self._authenticate

    @property
    def link(self):
        return self._link

    @property
    def unlink(self):
        return self._unlink
