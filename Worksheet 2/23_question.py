def greet(name):
    return f"Hello, {name}!"
say_hello = greet
print(say_hello("Harnoor"))
# passing functions to variable

def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x * x, 5)
print("Square:", result)
# passing function as arguments


def multiplier(factor):
    return lambda x: x * factor
double = multiplier(2)
triple = multiplier(3)
print("Double of 10:", double(10))
print("Triple of 10:", triple(10))
# returing fucntion to another function