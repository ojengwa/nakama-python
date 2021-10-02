import asyncio
from nakama import NakamaClient


async def test():
    client = NakamaClient('127.0.0.1', 7350, 'defaultkey')
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI0ZTY1ODE4Ny0xNzdkLTQxMDctYTgxZi04ZTk4ZDJhZDY1NTMiLCJ1c24iOiJlcHdyVXF3cFliIiwiZXhwIjoxNjMyMTcyNTg2fQ.HIpQEwcydSyGksC2Idb-F6tlZxMEekdpNuOamLa2gnI'
    client.session.token = token
    print(client.session.expires)
    print(client.session.username)
    print(client.session.user_id)
    print(client.session.vars)

    print(client.session.expired)

    await client.close()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())


if __name__ == '__main__':
    main()
