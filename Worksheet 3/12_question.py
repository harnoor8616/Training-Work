# Write a program to print the factorial of a number using a loop
num=int(input("Please enter a number:   "))
fact_num=1
def fact(num):
    global fact_num
    for i in range(1,num):
        fact_num=fact_num*i+fact_num
    return fact_num
print(fact(num))