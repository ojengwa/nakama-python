class Session():

    @property
    def expired(self):
        pass

    def __init__(self, client):
        self.client = client

        self.token = None
        self.expires = None
        self.username = None
        self.user_id = None
        self.vars = None

    def set_token(self, token):
        pass

    def set_basic(self, username, password):
        pass

    async def refresh(self):
        pass

    async def logout(self):
        pass
