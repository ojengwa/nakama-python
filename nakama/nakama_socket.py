import asyncio


class NakamaSocket():

    def __init__(self, client, **handlers):
        self.client = client
        self.websocket = None
        self.ws_listener_task = None

        self.handlers = {
            'notification': handlers.get('notification'),
            'match_data': handlers.get('match_data'),
            'match_presence': handlers.get('match_presence'),
            'matchmaker_matched': handlers.get('matchmaker_matched'),
            'status_presence': handlers.get('status_presence'),
            'stream_presence': handlers.get('stream_presence'),
            'stream_data': handlers.get('stream_data'),
            'channel_message': handlers.get('channel_message'),
            'disconnect': handlers.get('disconnect')
        }

    async def _websocket_listener(self, ws):
        while True:
            if ws.closed:
                handler = self.handlers['disconnect']
                handler()
                self.close()
                break

            msg = await ws.receive_json()
            print(msg)
            # сначала отловить события
            # Если сообщение не событие, то нужно отдать ответ

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
        # Разные методы под разные сообщения
        # Строка? Или байты? жсон.
        # кодировать сообщения матча
        await self.websocket.send_str(data)

    def set_notification_handler(self, handler):
        self.handlers['notification'] = handler

    def set_match_data_handler(self, handler):
        self.handlers['match_data'] = handler

    def set_match_presence_handler(self, handler):
        self.handlers['match_presence'] = handler

    def set_matchmaker_matched_handler(self, handler):
        self.handlers['matchmaker_matched'] = handler

    def set_status_presence_handler(self, handler):
        self.handlers['status_presence'] = handler

    def set_stream_presence_handler(self, handler):
        self.handlers['stream_presence'] = handler

    def set_stream_data_handler(self, handler):
        self.handlers['stream_data'] = handler

    def set_channel_message_handler(self, handler):
        self.handlers['channel_message'] = handler

    def set_disconnect_handler(self, handler):
        self.handlers['disconnect'] = handler
