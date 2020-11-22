#https://docs.aiohttp.org/en/stable/client_reference.html
async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.json()
