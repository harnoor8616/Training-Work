# Input two lists with the same values. Print their IDs and compare.
x = [1, 2, 3]
y = [1, 2, 3]
print("ID of x:", id(x))
print("ID of y:", id(y))
print("Are the IDs of x and y the same?", id(x) == id(y))