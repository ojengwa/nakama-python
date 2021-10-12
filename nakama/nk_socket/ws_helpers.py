class WSRequestWaiter():

    def __init__(self):
        self.res = None

    def __await__(self):
        while self.res is None:
            yield
        return self.res


class WSRequestHandler():

    def __init__(self):
        # TO DO: add timeouts to requests
        self.cid_count = 0
        self.requests = {}
        self.results = {}

    def get_cid(self):
        if len(self.requests.keys()) == 0:
            self.cid_count = 0
        self.cid_count += 1
        return self.cid_count

    def add_request(self, cid, request):
        res = self.results.get(cid)
        if res is None:
            self.requests[cid] = request
        else:
            request.res = res
            del self.results[cid]

    def handle_result(self, cid, result):
        waiter = self.requests.get(cid)
        if waiter is None:
            self.results[cid] = result
        else:
            waiter.res = result
            del self.requests[cid]
