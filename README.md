# Readme

This is a python module for retrieving stock prices for GNU Cash books.
The script uses `aiohttp` to fetch the price for your securities from
the Yahoo Finance API at the last close and adds it to your price database.  
Additionally it uses the [Forex API](https://theforexapi.com) to convert 
asset currencies to your local GNU Cash book currency.

**Note** the terms of use of the Yahoo API for developers
* [Yahoo Developer API Terms of Use](https://legal.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.html)
* [Yahoo Terms of Service](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html)
* [Yahoo Terms](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)

# Setup

## Requirements
* Requires Python >= 3.6 (due to `aiohttp`)
* Requires `pip` for dependency management

## Installation
```
python -m venv .env
.\.env\Scripts\activate
pip install -r requirements.txt
```

# Usage
```
python main.py --backend xml.gz --currency EUR .\database.gnucash
```
* `currency` represents the target currency of your GNU Cash book

# Limitations

1. Without a valid ISIN configured for your security the script will not 
   be able to fetch prices
1. The only backend that is currently supported is `xml.gz` files