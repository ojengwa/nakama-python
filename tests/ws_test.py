import asyncio
import json
from nakama import NakamaClient, NakamaSocket


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
    await socket.connect()
    data = {
        'cid': '5',
        'match_create': {}
    }
    #data = json.dumps(data)
    print('sending...')
    await socket.send(data)
    '''
    {
        'match':
            {
            'match_id': '3ce20d0d-d6d8-497a-aabd-dbf5f698dd4f.',
            'size': 1,
            'self':
                {
                    'user_id': '10c03663-420f-41b9-b3b0-58ccb8708bd7',
                    'session_id': 'cf13438c-2a06-11ec-aa86-7106fdcb5b46',
                    'username': 'testUser'
                }
            }
    }
    {
    'match_presence_event': {
        'match_id': '3ce20d0d-d6d8-497a-aabd-dbf5f698dd4f.',
        'joins': [{'user_id': '10c03663-420f-41b9-b3b0-58ccb8708bd7', 'session_id': 'cf13438c-2a06-11ec-aa86-7106fdcb5b46', 'username': 'testUser'}]}}
    '''
    while True:
        await asyncio.sleep(10)
    await socket.close()
    await client.close()


def main():
    asyncio.run(test())


if __name__ == '__main__':
    main()
