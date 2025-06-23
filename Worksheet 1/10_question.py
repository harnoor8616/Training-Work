# Try assigning small and large integers and compare IDs: a = 256, b = 256; c = 257, d = 257
# Assign small integers
a = 256  
b = 256
print("ID of a (256):", id(a))
print("ID of b (256):", id(b))
print("Are the IDs of a and b the same?", id(a) == id(b))
# Assign large integers
c = 257 
d = 257
print("ID of c (257):", id(c))
print("ID of d (257):", id(d))
print("Are the IDs of c and d the same?", id(c) == id(d))