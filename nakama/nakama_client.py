import aiohttp

from .account import Account
from .channel import Channel
from .event import Event
from .friends import Friends
from .groups import Groups
from .leaderboard import Leaderboard
from .matches import Matches
from .notifications import Notifications
from .purchase import Purchase
from .rpc import RPC
from .session import Session
from .storage import Storage
from .tournaments import Tournaments
from .user import User


class NakamaClient():

    def __init__(self, host, port, server_key, use_ssl=False):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl

        protocol = use_ssl and 'https' or 'http'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self._http_uri = '%s://%s:%d' % (protocol, host, port)
        self._http_session = aiohttp.ClientSession(headers=headers)

        self._account = Account(self)
        self._channel = Channel(self)
        self._event = Event(self)
        self._friends = Friends(self)
        self._groups = Groups(self)
        self._leaderboard = Leaderboard(self)
        self._matches = Matches(self)
        self._notifications = Notifications(self)
        self._purchase = Purchase(self)
        self._rpc = RPC(self)
        self._session = Session(self, server_key)
        self._storage = Storage(self)
        self._tournaments = Tournaments(self)
        self._user = User(self)

    async def close(self):
        await self._http_session.close()

    async def healthcheck(self):
        url_path = self._http_uri + '/healthcheck'
        headers = self.session.auth_header
        async with self._http_session.get(url_path, headers=headers) as resp:
            return await resp.json()

    @property
    def account(self):
        return self._account

    @property
    def user(self):
        return self._user

    @property
    def session(self):
        return self._session

    @property
    def matches(self):
        return self._matches

    @property
    def channel(self):
        return self._channel

    @property
    def friends(self):
        return self._friends

    @property
    def groups(self):
        return self._groups

    @property
    def leaderboard(self):
        return self._leaderboard

    @property
    def tournaments(self):
        return self._tournaments

    @property
    def notifications(self):
        return self._notifications

    @property
    def purchase(self):
        return self._purchase

    @property
    def storage(self):
        return self._storage

    @property
    def rpc(self):
        return self._rpc

    @property
    def event(self):
        return self._event
