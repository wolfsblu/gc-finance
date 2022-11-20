# Readme

This is a python module for retrieving stock prices for GNU Cash books.
The script uses `yfinance` to fetch the price for your securities at the last close and add it to your price database.

# Setup
```
python -m venv .env
.\.env\Scripts\activate
pip install -r requirements.txt
```

# Usage
```
python main.py --backend xml.gz --currency EUR .\database.gnucash
```

# Limitations

1. Due to how `yfinance.download` works there is no support for currencies as of yet (default is EUR)
1. Without a valid ISIN configured for your security the script will not be able to fetch prices
1. The only backend that is currently supported is `xml.gz` files