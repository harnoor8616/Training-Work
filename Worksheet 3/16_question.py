# Write a program that accepts a character and checks if it is a vowel or consonant.
character=input("Please enter a character:")
character1=character.upper()
if(character=="A" or character=="E" or character=="I" or character=="O" or character=="U" ):
    print(f"{character} is a vowel")
elif(character in ['*', '#', '@', '$', '%', '&', '^', '+', '=', '~', '!', '?', '/', '\\', '|', '_', '.', ':', '>', '<']):
    print(f"{character} is a symbol")
else:
    print(f"{character} is a consonent")