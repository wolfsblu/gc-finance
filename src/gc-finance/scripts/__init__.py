import asyncio

from argparse import ArgumentParser
from backends.factory import create_serializer
from dotenv import load_dotenv
from finance import get_tickers
from forex import convert
from gnucash import Price


load_dotenv()

parser = ArgumentParser()
parser.add_argument("-b", "--backend", type=str, default="xml.gz")
parser.add_argument("-c", "--currency", type=str, default="EUR")
parser.add_argument("filename")

async def main():
    args = parser.parse_args()
    serializer = create_serializer(args.backend, args.filename)

    stocks = serializer.get_stocks()
    xcodes = [stock.xcode for stock in stocks]
    tickers = await get_tickers(xcodes)

    prices = []
    for isin, chart in tickers:
        stock = next(item for item in stocks if item.xcode == isin)
        value = await convert(
            chart["regularMarketPrice"], 
            from_symbol = chart["currency"], 
            to_symbol = args.currency,
        )
        prices.append(Price(stock, args.currency, value))

    serializer.write_prices(prices)
    serializer.save()


if __name__ == "__main__":
    asyncio.run(main())