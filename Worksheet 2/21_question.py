# Write a lambda function to calculate the square of a number and use it in a loop.
square=lambda num :num * num
print(square,10)

for i in range(0,21):
    print(square(i))