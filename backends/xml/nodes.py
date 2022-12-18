PRICE_NODE = '''<price>
    <price:id type="guid">{id}</price:id>
    <price:commodity>
        <cmdty:space>Stocks</cmdty:space>
        <cmdty:id>{ticker}</cmdty:id>
    </price:commodity>
    <price:currency>
        <cmdty:space>CURRENCY</cmdty:space>
        <cmdty:id>{currency}</cmdty:id>
    </price:currency>
    <price:time>
        <ts:date>{date}</ts:date>
    </price:time>
    <price:source>gc-finance</price:source>
    <price:type>last</price:type>
    <price:value>{value}</price:value>
</price>'''
