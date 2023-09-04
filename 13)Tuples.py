# A tuple is a collection which is ordered and unchangeable and doesnt required uniquie values
# Create a Tuple:
singleItemTuple = ("AAPL",)
multiDataTypeTuple = ("abc", 34, True, 40, "male")
tuple = ("AAPL", "TSLA", "AMD")
print(tuple)
print(len(tuple))  # Tuple Length
print(type(singleItemTuple))  # type()
print(tuple[1])  # accesing 1st indexof list
print(tuple[-1])  # last item


# Since tuples are immutable we should change it into a list and then change it back to tuple
convertedToList = list(tuple)
print(convertedToList)
convertedToList[1] = "GME"
convertedToList.append("AMD")  # inserting
print(tuple)
