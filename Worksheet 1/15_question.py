# Assign a = 5.5 and b = float(5.5). Compare their IDs and explain the result
a = 5.5
b = float(5.5)
print("ID of a (5.5):", id(a))
print("ID of b (float(5.5)):", id(b))
print("Are the IDs of a and b the same?", id(a) == id(b))
