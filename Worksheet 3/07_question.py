#  Write a program to print a multiplication table of a given number
num=int(input("Please enter a number:   "))
for i in range(0,11):
    print(f"{num} X {i} = {num*i}")