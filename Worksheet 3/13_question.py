# Write a program to find the GCD of two numbers using loops
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 < num2:
    smaller = num1
else:
    smaller = num2
gcd = 1
for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i 
print(f"The GCD of {num1} and {num2} is: {gcd}")

