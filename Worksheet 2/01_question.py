# What is the difference between primitive and non-primitive data types in Python? Give examples
# primitve data types are immutable and non-primitive data types are mutable
# Primitive data types are the basic building blocks of data in Python. They include:
# 1. Integers (int): Whole numbers, e.g., 5, -10, 0
# 2. Floats (float): Decimal numbers, e.g., 3.14        
# 3. Strings (str): Sequences of characters, e.g., "Hello", 'World'
# 4. Booleans (bool): True or False values
# Non-primitive data types are more complex and can hold multiple values. They include:
# 1. Lists: Ordered collections of items, e.g., [1, 2, 3], ['apple', 'banana']
# 2. Tuples: Immutable ordered collections, e.g., (1, 2, 3), ('a', 'b')
# 3. Sets: Unordered collections of unique items, e.g., {1, 2, 3}, {'apple', 'banana'}
# 4. Dictionaries: Key-value pairs, e.g., {'name': 'Alice', 'age': 30}, {1: 'one', 2: 'two'}
a="Harnoor"
b=99
c=None
d=3.14
e=True
f=[1, 2, 3]
g=(1, 2, 3)
h={1, 2, 3}
i={'name': 'Alice', 'age': 30}
print(type(a))  # str
print(type(b))  # int
print(type(c))  # NoneType
print(type(d))  # float
print(type(e))  # bool
print(type(f))  # list
print(type(g))  # tuple
print(type(h))  # set
print(type(i))  # dict
