import asyncio
from nakama import NakamaClient


async def test():
    client = NakamaClient('127.0.0.1', 7350, 'defaultkey')
    print(await client.account.authenticate.custom('127888888'))
    '''
    {'created': True,
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI0ZTY1ODE4Ny0xNzdkLTQxMDctYTgxZi04ZTk4ZDJhZDY1NTMiLCJ1c24iOiJlcHdyVXF3cFliIiwiZXhwIjoxNjMyMTcyNTg2fQ.HIpQEwcydSyGksC2Idb-F6tlZxMEekdpNuOamLa2gnI',
    'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI0ZTY1ODE4Ny0xNzdkLTQxMDctYTgxZi04ZTk4ZDJhZDY1NTMiLCJ1c24iOiJlcHdyVXF3cFliIiwiZXhwIjoxNjMyMTY4OTg2fQ.A1_QuwJsar5dLmo6guoxp-4FWynfimHkXXww5XwrsLE'}
    '''
    await client.close()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())


if __name__ == '__main__':
    main()
