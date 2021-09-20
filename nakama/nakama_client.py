from nakama.account.account import Account
from nakama.channel import Channel
from nakama.friends import Friends
from nakama.groups import Groups
from nakama.leaderboard import Leaderboard
#from nakama.nakama_socket import NakamaSocket
from nakama.notifications import Notifications
from nakama.purchase import Purchase
from nakama.rpc import RPC
from nakama.session import Session
from nakama.storage import Storage
from nakama.tournaments import Tournaments
from nakama.user import User


class NakamaClient():

    def __init__(self, host, port, timeout=0, use_ssl=False):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.use_ssl = use_ssl

        self._account = Account(self)
        self._channel = Channel(self)
        self._friends = Friends(self)
        self._groups = Groups(self)
        self._leaderboard = Leaderboard(self)
        self._notifications = Notifications(self)
        self._purchase = Purchase(self)
        self._rpc = RPC(self)
        self._session = Session(self)
        self._storage = Storage(self)
        self._tournaments = Tournaments(self)
        self._user = User(self)

    async def healthcheck(self):
        pass

    async def event(self, name, properties):
        pass

    async def match(self):
        pass

    #def create_socket(self):
        #pass

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
