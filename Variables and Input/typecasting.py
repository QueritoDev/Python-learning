# Typecasting = the process of converting a variable from one data 
# type to another
#       str(), int(), float(), bool()


name = "Aly"
age = 18
gpa = 3.2
is_student = True

gpa = int(gpa)
print(gpa)

age = str(age)
print(age)
print("Type of age:",type(age))

# Typecast str to bool
name = bool(name)
print(name)

name = ""
name = bool(name)
print(name)