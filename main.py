from argparse import ArgumentParser
from backends.factory import create_serializer
from finance import get_prices
from gnucash import Price

parser = ArgumentParser()
parser.add_argument("-b", "--backend", type=str, default="xml.gz")
parser.add_argument("-c", "--currency", type=str, default="EUR")
parser.add_argument("filename")

def main():
    args = parser.parse_args()
    serializer = create_serializer(args.backend, args.filename)

    stocks = serializer.get_stocks()
    xcodes = [stock.xcode for stock in stocks]
    raw_prices = get_prices(xcodes)

    prices = []
    for stock in stocks:
        prices.append(
            Price(
                stock=stock,
                currency=args.currency,
                value=raw_prices['Close'][stock.xcode].item()
            )
        )

    serializer.write_prices(prices)
    serializer.save()

if __name__ == "__main__":
    main()