# unordered, unchangeable*, and unindexed
# Duplicates Not Allowed
set = {"AAPL", "AMD", "NVDA"}
print(set)

print(len(set))  # Length of a Set
print(type(set))  # type()


# Access Items
# You cannot access items in a set by referring to an index or a key as its unindexed


# Add items
set.add("TSLA")
print(set)

# Join Two Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
