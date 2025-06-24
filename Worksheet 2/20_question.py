def func(name):
    return(f"hello ,{name}")
x=func
print(x("Karan"))

# passing function to variable
def func1(name1):
    return(f"hello {name1}")

def call_func1(func1,name1):
    result=func(name1)
    print(result)

call_func1(func1,"Harnoor")

# passing function as argument 
