#implicit
x = 32 # integer
y = 5.3 # float

result = x + y
print(result, "of type", type(result))

a = 5 #integer
b = "3" #string


#explicit
result1 = a * int(b)
print(result1, "of type",type(result1))

age = 35
age_string = str(25)
print(age_string, "of type", type(age_string))

print(bool(0))
print(bool(50))

print(bool(""))
print(bool("hello"))