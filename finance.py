import yfinance as yf


def get_prices(stocks, period="1d"):
    return yf.download(
        tickers = " ".join(stocks),
        period  = period
    )