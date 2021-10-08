import asyncio
from nakama import NakamaClient


async def test():
    client = NakamaClient('127.0.0.1', 7350, 'defaultkey')
    res = await client.account.authenticate.custom('127888888',
                                                   create='true',
                                                   username='testUser',
                                                   vars={
                                                    'test': '123'
                                                   })
    token = res['token']
    refresh_token = res['refresh_token']
    client.session.token = token
    client.session.refresh_token = refresh_token
    print(await client.account.get())
    await client.close()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())


if __name__ == '__main__':
    main()
