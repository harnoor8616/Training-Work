#  Write a program to print all prime numbers between 1 and 100.
print("Prime numbers between 1 and 100 are:")
for num in range(2, 101): 
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")