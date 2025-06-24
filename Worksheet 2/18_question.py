# Create a function that uses a global variable and modifies it
x=10
def outer():
    global x
    x=x+1
    print(x)
outer()
print(x)
