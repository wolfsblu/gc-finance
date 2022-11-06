from requests import get

def get_rate(from_symbol, to_symbol):
    url = f"https://theforexapi.com/api/latest?base={from_symbol}&symbols={to_symbol}"
    forex_request = get(url)
    forex_response = forex_request.json()
    rate = forex_response["rates"][to_symbol]
    return rate