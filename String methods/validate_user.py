# validate user input exercise
# 1. userusername is no more than 12 characters
# 2. userusername must not contain spaces
# 3. userusername must not contain digits

username = input("Enter your userusername: ")
haveSpace = username.count(" ")
haveDigit = username.isalpha()

print(haveDigit)


if len(username)>12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")


