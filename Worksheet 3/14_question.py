#  Write a program to display the Fibonacci series up to n terms
n = int(input("How many terms? "))
first = 0
second = 1
for i in range(n):
    print(first, end=" ")
    next = first + second
    first = second
    second = next
