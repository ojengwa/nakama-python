import base64


class Handlers():

    async def _empty_handler(self, event):
        pass

    def __init__(self):
        self.notification_handler = self._empty_handler
        self.match_data_handler = self._empty_handler
        self.match_presence_handler = self._empty_handler
        self.matchmaker_matched_handler = self._empty_handler
        self.status_presence_handler = self._empty_handler
        self.stream_presence_handler = self._empty_handler
        self.stream_data_handler = self._empty_handler
        self.channel_message_handler = self._empty_handler
        self.channel_presence_handler = self._empty_handler
        self.disconnect_handler = self._empty_handler

    async def handle_event(self, type, event):
        if type == 'notifications':
            # TO DO: maybe separate tasks for each ntf?
            for ntf in event:
                await self.notification_handler(ntf)
        elif type == 'match_data':
            event.data = event.data.encode()
            pad = len(event.data) % 4
            event.data += b"="*pad  # correct padding
            event.data = base64.b64decode(event.data)
            await self.match_data_handler(event)
        elif type == 'match_presence_event':
            await self.match_presence_handler(event)
        elif type == 'matchmaker_matched':
            await self.matchmaker_matched_handler(event)
        elif type == 'status_presence_event':
            await self.status_presence_handler(event)
        elif type == 'stream_presence_event':
            await self.stream_presence_handler(event)
        elif type == 'stream_data':
            await self.stream_data_handler(event)
        elif type == 'channel_message':
            await self.channel_message_handler(event)
        elif type == 'channel_presence_event':
            await self.channel_presence_handler(event)
        elif type == 'disconnect':
            await self.disconnect_handler(event)

    def set_notification_handler(self, handler):
        self.notification_handler = handler or self._empty_handler

    def set_match_data_handler(self, handler):
        self.match_data_handler = handler or self._empty_handler

    def set_match_presence_handler(self, handler):
        self.match_presence_handler = handler or self._empty_handler

    def set_matchmaker_matched_handler(self, handler):
        self.matchmaker_matched_handler = handler or self._empty_handler

    def set_status_presence_handler(self, handler):
        self.status_presence_handler = handler or self._empty_handler

    def set_stream_presence_handler(self, handler):
        self.stream_presence_handler = handler or self._empty_handler

    def set_stream_data_handler(self, handler):
        self.stream_data_handler = handler or self._empty_handler

    def set_channel_message_handler(self, handler):
        self.channel_message_handler = handler or self._empty_handler

    def set_channel_presence_handler(self, handler):
        self.channel_presence_handler = handler or self._empty_handler

    def set_disconnect_handler(self, handler):
        self.disconnect_handler = handler or self._empty_handler
