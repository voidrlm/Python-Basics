# Create a list
stocks = ["AAPL", "TSLA", "NVDA"]
multiDataTypes = ["abc", 12, True, 34, "def"]
print(stocks)
print(multiDataTypes)
print("length {}".format(len(stocks)))  # length of list
print(stocks[1])  # accesing 1st indexof list
print(stocks[-1])  # last item
stocks[1] = "COIN"  # changing value in list
print(stocks)
stocks.insert(2, "AMD")  # inserting
print(stocks)
