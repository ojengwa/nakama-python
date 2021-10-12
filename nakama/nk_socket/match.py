import base64
from .ws_helpers import WSRequestWaiter


class Match():

    def __init__(self, socket):
        self.ws = socket
        self.rq_handler = socket.request_handler

    async def create(self):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        message = {
            'cid': cid,
            'match_create': {}
        }
        await self.ws.send(message)
        return await rq_waiter

    async def join(self, match_id, token=None, metadata=None):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'match_id': match_id
        }
        if token is not None:
            data['token'] = token
        if metadata is not None:
            data['metadata'] = metadata

        message = {
            'cid': cid,
            'match_join': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def leave(self, match_id):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'match_id': match_id
        }

        message = {
            'cid': cid,
            'match_leave': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def send_data(self, match_id, op_code, m_data):
        assert isinstance(m_data, str), 'Match data must be string!'

        m_data = m_data.encode()
        m_data = base64.b64encode(m_data)
        data = {
            'match_id': match_id,
            'op_code': op_code,
            'data': m_data.decode()
        }

        message = {
            'match_data_send': data
        }
        await self.ws.send(message)
