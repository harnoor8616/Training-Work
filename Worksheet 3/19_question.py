# Write a program to reverse a given number using a loop
num = input("Enter a number: ")
reverse = ""
for digit in num:
    reverse = digit + reverse 
print("Reversed number is:", reverse)
