class RPC():

    def __init__(self, client):
        self.client = client

    def __getattr__(self, name):
        pass
