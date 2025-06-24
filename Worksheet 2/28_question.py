# Write a program that counts the number of vowels in a given string using a loop.
string="HarnoorKaurDhiman"
string=string.lower()
count=0
for i in string:
    if(i=="a"or i=="e"or i=="i"or i=="o"or i=="u"):
        count=count+1
print(count)