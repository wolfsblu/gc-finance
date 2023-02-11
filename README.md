# Readme

This is a python module retrieving stock prices for GNU Cash books.
The script uses `aiohttp` to fetch the prices of your securities from
the Yahoo Finance API and adds them to your price database. Additionally
it uses the [Tradermade API](https://tradermade.com/forex) to convert asset 
currencies to your local GNU Cash book currency.

**Note** the terms of use of the Yahoo API for developers
* [Yahoo Developer API Terms of Use](https://legal.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.html)
* [Yahoo Terms of Service](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html)
* [Yahoo Terms](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)

# Setup

## Requirements
* Requires Python >= 3.6 (due to `aiohttp`)
* Requires `pip` for dependency management
* A (free) API key for the Tradermade forex API

## Installation
1. Install dependencies  
   ```
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```
1. Copy the `.env.example` file to `.env` and add your API key

# Usage
```
python main.py --backend xml.gz --currency EUR .\database.gnucash
```
* `currency` represents the target currency of your GNU Cash book

# Limitations

1. Without a valid ISIN configured for your asset the script will not 
   be able to fetch prices
1. The only backend that is currently supported is `xml.gz` files