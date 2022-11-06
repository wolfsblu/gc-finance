from finance import get_prices
from gnucash import Book
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("filename")

def main():
    args = parser.parse_args()
    book = Book(args.filename)
    stocks = book.get_stocks()
    isins = [stock.isin for stock in stocks]
    prices = get_prices(isins)
    for isin in isins:
        print(prices["Close"][isin])


if __name__ == "__main__":
    main()