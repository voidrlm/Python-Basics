# Convert string to upper case
a = "test"
print(a.upper())

# Convert string to lower case
b = "TEST"
print(b.upper())

# Remove white space
c = "Test Test"
print(c.strip())

# Split string
d = "Test,Test"
print(d.split(","))
print(d.split(",")[0])


# Concatenate string
e = "concatenated"
f = "string"
g = e + f
print(g)


# Formatting
h = 1
i = 2
k = 3
myorder = "1){} 2) {} 3) {}"
print(myorder.format(h, i, k))
