import aiohttp
import json
import os


rates = dict()

async def get_rate(from_symbol, to_symbol, session):
    key = f"{from_symbol}-{to_symbol}"
    if key in rates:
        return rates[key]

    api_key = os.environ.get("FOREX_API_KEY")
    from_symbol = from_symbol.upper()
    to_symbol = to_symbol.upper()
    url = f"https://marketdata.tradermade.com/api/v1/convert?api_key={api_key}&from={from_symbol}&to={to_symbol}&amount=1"
    async with session.get(url) as resp:
        text = await resp.text()
        data = json.loads(text)
        rate = data["quote"]
        rates[key] = rate
        return rate

async def convert(value, from_symbol="USD", to_symbol="USD"):
    if from_symbol == to_symbol:
        return value
    async with aiohttp.ClientSession() as session:
        rate = await get_rate(from_symbol, to_symbol, session)
        return value * rate