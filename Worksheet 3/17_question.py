# Write a program to calculate the power of a number using a loop
number=int(input("Please enter a number"))
power=int(input("Please enter a power"))
value=1
for i in range(0,power):
    value =value * number
print(value)