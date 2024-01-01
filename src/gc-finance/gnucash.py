class Stock:
    def __init__(self, ticker, name, xcode):
        self.ticker = ticker
        self.name = name
        self.xcode = xcode
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.ticker


class Price:
    def __init__(self, stock, currency, value):
        self.stock = stock
        self.currency = currency
        self.value = value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.stock.ticker} {self.value}{self.currency}"