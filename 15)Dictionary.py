stock = {"name": "Apple", "symbol": "AAPL", "price": 200}
print(stock)

print(stock["name"])
print(len(stock))  # length
stock.keys()  # key values alone

# changing items
stock["name"] = "Tesla"
stock["symbol"] = "TSLA"
stock["price"] = "TSLA"
print(stock)

# add items
stock["marketCap"] = "1T"
print(stock)
# remove
stock.pop("marketCap")
print(stock)
