# Take an input age and print whether the person is a child, teenager, adult, or senior.
age=int(input("Enter your age:\n"))
if(age>=0 and age<=12):
    print('You are a child')
elif(age>=13 and age<=19):
    print('You are a teenager')
elif(age>=20 and age<=59):
    print('You are a adult')
elif(age>=59):
    print('You are a senior')