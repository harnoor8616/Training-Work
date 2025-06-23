# Use a loop to print all numbers from 1 to 20, except multiples of 5 (use continue).
for i in range(1,21):
    if(i%5==0):
        continue;
    print(i)