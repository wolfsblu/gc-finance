import aiohttp
import asyncio


BASE_URL = "https://query1.finance.yahoo.com"

async def get_tickers(isins):
    async with aiohttp.ClientSession() as session:
        symbols = await asyncio.gather(*[get_symbol(isin, session) for isin in isins])
        charts = await asyncio.gather(*[get_chart(symbol, session) for symbol in symbols])
        return zip(isins, charts)

async def get_symbol(isin, session):
    url = f"{BASE_URL}/v1/finance/search?q={isin}"
    async with session.get(url) as resp:
        data = await resp.json()
        quotes = data.get("quotes", [{}])[0]
        return quotes["symbol"]

async def get_chart(symbol, session):
    url = f"{BASE_URL}/v8/finance/chart/{symbol}?range=1d&interval=1d"
    async with session.get(url) as resp:
        data = await resp.json()
        meta = data["chart"]["result"][0]["meta"]
        return meta