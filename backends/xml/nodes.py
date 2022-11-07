PRICE_NODE = '''<price xmlns:cmdty="http://www.gnucash.org/XML/cmdty" 
    xmlns:price="http://www.gnucash.org/XML/price" 
    xmlns:ts="http://www.gnucash.org/XML/ts">
    <price:id type="guid">{id}</price:id>
    <price:commodity>
        <cmdty:space>Stocks</cmdty:space>
        <cmdty:id>AMD</cmdty:id>
    </price:commodity>
    <price:currency>
        <cmdty:space>CURRENCY</cmdty:space>
        <cmdty:id>EUR</cmdty:id>
    </price:currency>
    <price:time>
        <ts:date>2022-11-03 10:59:00 +0000</ts:date>
    </price:time>
    <price:source>user:price-editor</price:source>
    <price:type>last</price:type>
    <price:value>9999</price:value>
</price>'''
