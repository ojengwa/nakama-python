import asyncio

from .handlers import Handlers
from .channel import Channel
from .match import Match
from .matchmaker import MatchMaker
from .status import Status


class NakamaSocket():

    @property
    def handlers(self):
        return self._handlers

    @property
    def channel(self):
        return self._channel

    @property
    def match(self):
        return self._match

    @property
    def matchmaker(self):
        return self._matchmaker

    @property
    def status(self):
        return self._status

    def __init__(self, client):
        self.client = client

        self.websocket = None
        self.ws_listener_task = None

        self._handlers = Handlers()
        self._channel = Channel(self)
        self._match = Match(self)
        self._matchmaker = MatchMaker(self)
        self._status = Status(self)

    async def _websocket_listener(self, ws):
        while True:
            if ws.closed:
                await self.handlers.handle('disconnect', None)
                await self.close()
                break

            msg = await ws.receive_json()
            print(msg)
            if msg.get('cid') is not None:
                pass
                # Если есть cid - значит, кто-то ждет ответа
            else:
                pass
                # Это обычное событие

    async def connect(self, loop=None):
        assert self.client.session.token is not None, 'You must set session.token'

        if loop is None:
            loop = asyncio.get_running_loop()

        url_path = self.client._http_uri + ('/ws?token=%s' %
                                            self.client.session.token)
        self.websocket = await self.client._http_session.ws_connect(url_path)

        self.ws_listener_task = loop.create_task(self._websocket_listener(self.websocket))

    async def close(self):
        assert self.websocket is not None, 'You must connect() before close'
        self.ws_listener_task.cancel()
        self.ws_listener_task = None
        await self.websocket.close()
        self.websocket = None

    async def send(self, data):
        assert self.websocket is not None, 'You must connect() before sending'
        await self.websocket.send_json(data)
