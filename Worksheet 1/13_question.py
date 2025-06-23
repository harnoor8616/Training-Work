# Create tuples a = (1, 2, 3), b = (1, 2, 3). Compare their IDs.
a = (1, 2, 3)
b = (1, 2, 3)
print("ID of a:", id(a))
print("ID of b:", id(b))
print("Are the IDs of a and b the same?", id(a) == id(b))
