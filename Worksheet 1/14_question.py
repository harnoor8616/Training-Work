# Store a string and an integer in variables. Reassign new values and check if ID changes.
x="Harnoor"
y= 20
print("ID of x:", id(x))
print("ID of y:", id(y))
x= "Harnoor Singh"
y= 30
print("ID of x after change:", id(x))
print("ID of y after change:", id(y))
