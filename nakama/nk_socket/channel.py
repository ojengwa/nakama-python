from .ws_helpers import WSRequestWaiter


class Channel():

    def __init__(self, socket):
        self.ws = socket
        self.rq_handler = socket.request_handler

    async def send_message(self, channel_id, content):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'channel_id': channel_id,
            'content': content
        }

        message = {
            'cid': cid,
            'channel_message_send': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def update_message(self, channel_id, message_id, content):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'channel_id': channel_id,
            'message_id': message_id,
            'content': content
        }

        message = {
            'cid': cid,
            'channel_message_update': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def delete_message(self, channel_id, message_id):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'channel_id': channel_id,
            'message_id': message_id
        }

        message = {
            'cid': cid,
            'channel_message_remove': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def join(self, target, type, persistence, hidden):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'target': target,
            'type': type,
            'persistence': persistence,
            'hidden': hidden
        }

        message = {
            'cid': cid,
            'channel_join': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def leave(self, channel_id):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'channel_id': channel_id
        }

        message = {
            'cid': cid,
            'channel_leave': data
        }
        await self.ws.send(message)
        return await rq_waiter
