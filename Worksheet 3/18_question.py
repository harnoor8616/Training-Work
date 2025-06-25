# Write a program to find the sum of digits of a number
num = input("Please enter a number: ")
digit_sum = 0
for i in num:
    digit_sum += int(i)
print("Sum of digits:", digit_sum)