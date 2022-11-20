PRICE_NODE = '''<price>
    <price:id type="guid">{id}</price:id>
    <price:commodity>
        <cmdty:space>Stocks</cmdty:space>
        <cmdty:id>{ticker}</cmdty:id>
    </price:commodity>
    <price:currency>
        <cmdty:space>CURRENCY</cmdty:space>
        <cmdty:id>EUR</cmdty:id>
    </price:currency>
    <price:time>
        <ts:date>{date}</ts:date>
    </price:time>
    <price:source>user:price-editor</price:source>
    <price:type>last</price:type>
    <price:value>{value}</price:value>
</price>'''
