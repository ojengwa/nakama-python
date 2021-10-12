from .ws_helpers import WSRequestWaiter


class Status():

    def __init__(self, socket):
        self.ws = socket
        self.rq_handler = socket.request_handler

    async def follow(self, user_ids):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'user_ids': user_ids
        }

        message = {
            'cid': cid,
            'status_follow': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def unfollow(self, user_ids):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'user_ids': user_ids
        }

        message = {
            'cid': cid,
            'status_unfollow': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def update(self, status):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'status': status
        }

        message = {
            'cid': cid,
            'status_update': data
        }
        await self.ws.send(message)
        return await rq_waiter
