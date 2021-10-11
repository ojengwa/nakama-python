import asyncio


class Awaitable:

    def __init__(self):
        self.num = 0

    def __await__(self):
        while True:
            if self.num == 50:
                return 88
            print('aa: %s' % self.num)
            self.num += 1
            yield


async def main():
    print(await Awaitable())


asyncio.run(main())
