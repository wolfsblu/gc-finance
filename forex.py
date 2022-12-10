import aiohttp
import json


async def get_rate(from_symbol, to_symbol, session):
    url = f"https://theforexapi.com/api/latest?base={from_symbol}&symbols={to_symbol}"
    async with session.get(url) as resp:
        text = await resp.text()
        data = json.loads(text)
        rate = data["rates"][to_symbol]
        return rate

async def convert(value, from_symbol="USD", to_symbol="USD"):
    if from_symbol == to_symbol:
        return value
    async with aiohttp.ClientSession() as session:
        rate = await get_rate(from_symbol, to_symbol, session)
        return value * rate