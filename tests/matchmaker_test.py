import asyncio
from nakama import NakamaClient, NakamaSocket


async def matchmaker_matched(event):
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
    socket.handlers.set_matchmaker_matched_handler(matchmaker_matched)
    await socket.connect()
    print('pls wait...')
    ticket = await socket.matchmaker.add('*', 2, 4)
    ticket = ticket['matchmaker_ticket']['ticket']
    print('answer:', ticket)
    print('answer 2:', await socket.matchmaker.delete(ticket))
    await asyncio.sleep(3)
    await socket.close()
    await client.close()


def main():
    asyncio.run(test())


if __name__ == '__main__':
    main()
