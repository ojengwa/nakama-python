class Channel():

    def __init__(self, socket):
        self.ws = socket

    async def send_message(self):
        pass

    async def update_message(self):
        pass

    async def delete_message(self):
        pass

    async def join(self):
        pass

    async def leave(self):
        pass
