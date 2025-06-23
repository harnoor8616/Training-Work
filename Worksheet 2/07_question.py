# Check if the number 4 is both greater than 2 and less than 10 using logical operators.
a = 4
if(a>2):
    if(a<10):
        print(f"{a} is greater than both 2 and 10")
    else:
        print(f"{a} is not greater 10")
else:
    print(f"{a} is not greater than both 2 and 10")