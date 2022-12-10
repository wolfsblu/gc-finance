import gzip
import shutil
import tempfile
import uuid
import os
import xml.etree.ElementTree as ET
import mmap

from datetime import datetime, timezone
from backends.xml.nodes import PRICE_NODE
from gnucash import Stock


class Serializer:
    def __init__(self, filename):
        self.filename = filename
        with gzip.open(filename, 'rb') as compressed_file:
            with tempfile.TemporaryFile('r+b', delete=False) as self.temp_file:
                shutil.copyfileobj(compressed_file, self.temp_file)

    def __del__(self):
        if self.temp_file is not None and os.path.isfile(self.temp_file.name):
            os.remove(self.temp_file.name)

    def get_stocks(self):
        stocks = []
        for _, elem in ET.iterparse(self.temp_file.name):
            space = elem.find("{http://www.gnucash.org/XML/cmdty}space")
            if elem.tag == "{http://www.gnucash.org/XML/gnc}commodity" and space.text == "Stocks":
                ticker = elem.find("{http://www.gnucash.org/XML/cmdty}id").text
                name = elem.find("{http://www.gnucash.org/XML/cmdty}name").text
                isin = elem.find("{http://www.gnucash.org/XML/cmdty}xcode").text
                stocks.append(Stock(ticker, name, isin))
        return stocks

    def __get_price_pos(self, mmapped_file):
        original_pos = mmapped_file.tell()
        pricedb_pos = mmapped_file.find(b"pricedb")
        mmapped_file.seek(pricedb_pos)
        target_pos = mmapped_file.find(b"\n") + 1
        mmapped_file.seek(original_pos)
        return target_pos

    def __build_price_text(self, prices):
        now = datetime.now(timezone.utc)
        price_nodes = []
        for price in prices:
            price_nodes.append(
                PRICE_NODE.format(
                    currency=price.currency,
                    date=now.strftime("%Y-%m-%d %H:%M:%S %z"),
                    id=uuid.uuid4().hex,
                    ticker=price.stock.ticker,
                    value="{:.2f}".format(price.value)
                )
            )
        return os.linesep.join(price_nodes) + os.linesep

    def write_prices(self, prices):
        price_text = self.__build_price_text(prices)
        with open(self.temp_file.name, 'r+', encoding='utf-8') as f:
            price_bytes = str.encode(price_text, encoding="utf-8")
            file_size = os.path.getsize(f.name)
            os.ftruncate(f.fileno(), file_size + len(price_bytes))
            with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmapped_file:
                target_pos = self.__get_price_pos(mmapped_file)
                mmapped_file.move(target_pos + len(price_bytes), target_pos, file_size - target_pos)
                mmapped_file.seek(target_pos)
                mmapped_file.write(price_bytes)
                mmapped_file.flush()
    
    def save(self):
        with open(self.temp_file.name, 'rb') as f:
            with gzip.open(self.filename, 'wb') as compressed_file:
                shutil.copyfileobj(f, compressed_file)