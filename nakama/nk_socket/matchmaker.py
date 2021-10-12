from .ws_helpers import WSRequestWaiter


class MatchMaker():

    def __init__(self, socket):
        self.ws = socket
        self.rq_handler = socket.request_handler

    async def add(self, query, min_count, max_count,
                  string_properties=None, numeric_properties=None):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'query': query,
            'min_count': min_count,
            'max_count': max_count
        }
        if string_properties is not None:
            data['string_properties'] = string_properties
        if numeric_properties is not None:
            data['numeric_properties'] = numeric_properties

        message = {
            'cid': cid,
            'matchmaker_add': data
        }
        await self.ws.send(message)
        return await rq_waiter

    async def delete(self, ticket):
        cid = '%d' % self.rq_handler.get_cid()
        rq_waiter = WSRequestWaiter()
        self.rq_handler.add_request(cid, rq_waiter)

        data = {
            'ticket': ticket
        }

        message = {
            'cid': cid,
            'matchmaker_remove': data
        }
        await self.ws.send(message)
        return await rq_waiter
