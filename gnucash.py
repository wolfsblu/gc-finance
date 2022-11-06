import gzip
import tempfile
import shutil
import xml.etree.ElementTree as ET


class Stock:
    def __init__(self, ticker, name, isin):
        self.ticker = ticker
        self.name = name
        self.isin = isin
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.ticker


class XmlReader:
    def __init__(self, filename):
        self.filename = filename
        with gzip.open(filename, 'rb') as compressed_file:
            self.temp_file = tempfile.TemporaryFile('r+b', delete=False)
            shutil.copyfileobj(compressed_file, self.temp_file)
        self.temp_file.seek(0)

    def get_stocks(self):
        assets = []
        for _, elem in ET.iterparse(self.temp_file):
            space = elem.find("{http://www.gnucash.org/XML/cmdty}space")
            if elem.tag == "{http://www.gnucash.org/XML/gnc}commodity" and space.text == "Stocks":
                ticker = elem.find("{http://www.gnucash.org/XML/cmdty}id").text
                name = elem.find("{http://www.gnucash.org/XML/cmdty}name").text
                isin = elem.find("{http://www.gnucash.org/XML/cmdty}xcode").text
                assets.append(Stock(ticker, name, isin))
        return assets


class Book:
    def __init__(self, filename):
        self.reader = XmlReader(filename)
    
    def get_stocks(self):
        return self.reader.get_stocks()