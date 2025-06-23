# Assign a = 'hello', b = 'hello', c = 'HELLO'. Print all IDs. Which are same and which are different?
a = 'hello'
b = 'hello'
c = 'HELLO'
print("ID of a:", id(a))
print("ID of b:", id(b))    
print("ID of c:", id(c))
print("Are the IDs of a and b the same?", id(a) == id(b))   
print("Are the IDs of a and c the same?", id(a) == id(c))
print("Are the IDs of b and c the same?", id(b) == id(c))