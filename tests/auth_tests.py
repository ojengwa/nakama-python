import asyncio
from nakama import NakamaClient


async def test():
    client = NakamaClient('127.0.0.1', 7350, 'defaultkey')
    await auth_custom_test(client)
    await auth_email_test(client)
    await auth_device_test(client)
    await client.close()


async def auth_custom_test(client):
    print(await client.account.authenticate.custom('127888888',
                                                   create='true',
                                                   username='testUser',
                                                   vars={
                                                    'test': '123'
                                                   }))
    '''
    {'created': True,
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI0ZTY1ODE4Ny0xNzdkLTQxMDctYTgxZi04ZTk4ZDJhZDY1NTMiLCJ1c24iOiJlcHdyVXF3cFliIiwiZXhwIjoxNjMyMTcyNTg2fQ.HIpQEwcydSyGksC2Idb-F6tlZxMEekdpNuOamLa2gnI',
    'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI0ZTY1ODE4Ny0xNzdkLTQxMDctYTgxZi04ZTk4ZDJhZDY1NTMiLCJ1c24iOiJlcHdyVXF3cFliIiwiZXhwIjoxNjMyMTY4OTg2fQ.A1_QuwJsar5dLmo6guoxp-4FWynfimHkXXww5XwrsLE'}
    '''


async def auth_email_test(client):
    print(await client.account.authenticate.email('tester@email.com',
                                                  'bbccddeeff'))


async def auth_device_test(client):
    print(await client.account.authenticate.device('9999999999'))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())


if __name__ == '__main__':
    main()
