import gzip
import shutil
import tempfile
import uuid
import xml.etree.ElementTree as ET

from .namespaces import register_namespaces
from .nodes import PRICE_NODE

from gnucash import Stock


class Serializer:
    def __init__(self, filename):
        register_namespaces()
        self.filename = filename
        with gzip.open(filename, 'rb') as compressed_file:
            self.temp_file = tempfile.TemporaryFile('r+b', delete=False)
            shutil.copyfileobj(compressed_file, self.temp_file)
        self.temp_file.seek(0)

    def get_stocks(self):
        stocks = []
        for _, elem in ET.iterparse(self.temp_file):
            space = elem.find("{http://www.gnucash.org/XML/cmdty}space")
            if elem.tag == "{http://www.gnucash.org/XML/gnc}commodity" and space.text == "Stocks":
                ticker = elem.find("{http://www.gnucash.org/XML/cmdty}id").text
                name = elem.find("{http://www.gnucash.org/XML/cmdty}name").text
                isin = elem.find("{http://www.gnucash.org/XML/cmdty}xcode").text
                stocks.append(Stock(ticker, name, isin))
        return stocks

    def write_prices(self, tree, prices):
        prices = tree.find(".//{http://www.gnucash.org/XML/gnc}pricedb")
        content = ET.fromstring(PRICE_NODE.format(
            id=uuid.uuid4().hex)
        )
        prices.append(content)

    def write(self):
        tree = ET.parse(self.temp_file)
        self.temp_file.seek(0)
        self.write_prices(tree, [])
        tree.write(self.temp_file, encoding="utf-8")
        self.temp_file.truncate()