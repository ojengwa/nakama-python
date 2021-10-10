import asyncio
import aiohttp

async def test():
    out_headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    in_headers={'TEST': 'ofofof'}
    async with aiohttp.ClientSession(headers=out_headers) as session:
        async with session.get("http://httpbin.org/headers", headers=in_headers) as r:
            json_body = await r.json()
            print(json_body)

        ws = await session.ws_connect('http://httpbin.org/headers')
        ws.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
