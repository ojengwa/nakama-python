import asyncio
from nakama import NakamaClient, NakamaSocket


async def match_presence(event):
    print('handler:', event)


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

    socket = NakamaSocket(client)
    socket.handlers.set_match_presence_handler(match_presence)
    await socket.connect()
    print('pls wait...')
    answer = await socket.match.create()
    print('answer:', answer)
    match_id = answer['match']['match_id']
    print('match_data answer:', await socket.match.send_data(match_id, 88, 'y'))
    await asyncio.sleep(3)
    await socket.close()
    await client.close()


def main():
    asyncio.run(test())


if __name__ == '__main__':
    main()
