# Input the same string in two different variables and compare their id. Then change one value and compare again.
x="Harnoor"
y="Harnoor"
print("ID of x:", id(x))
print("ID of y:", id(y))
x= "Harnoor Singh"
print("ID of x after change:", id(x))
print("ID of y after change:", id(y))