# Store a lambda function inside a dictionary and call it.
dict={"square": lambda x: x*x}
number=10
print(dict['square'](number))