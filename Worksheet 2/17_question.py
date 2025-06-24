# Explain lexical scope with an example function
def outer_function():
    x=10
    def inner_function():
        x=11
        print(f"inner x:{x}")
    print(f"outer x:{x}")
    inner_function()
outer_function()