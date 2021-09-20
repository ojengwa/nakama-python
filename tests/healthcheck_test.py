import asyncio
from nakama import NakamaClient


async def test():
    client = NakamaClient('127.0.0.1', 7350, 'defaultkey')
    print(await client.healthcheck())
    await client.close()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())


if __name__ == '__main__':
    main()
