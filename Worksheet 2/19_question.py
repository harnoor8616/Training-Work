# Write a function with a nested inner function and use `nonlocal` to modify its variable.
def outer():
    a="Hwlo"
    def inner():
        nonlocal a
        print(a)
        a="Hello"
        print(a)
    print(a)
    inner()
outer()
