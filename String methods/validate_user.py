# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Enter your username: ")
haveSpace = name.count(" ")
haveDigit = name.isalpha()
print(haveDigit)

while haveSpace>0:
    print("Your username must not contain spaces!")
    name = input("Enter your username again: ")
    haveDigit = name.isalpha()
    print(haveDigit)

while haveDigit==False:
    print("Your username must not contain digits!")
    name = input("Enter your username again: ")
    haveDigit = name.isalpha()
