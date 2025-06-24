# Write a function with default and keyword arguments to print a greeting message.
def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")
greet()
greet("Harnoor")  
greet(greeting="Welcome", name="Raj")  
