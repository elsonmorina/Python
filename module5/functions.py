def greet():
    print("Hello World")
greet()


def greet_person(name):
    print("Hello",name)
greet_person("Alice")
greet_person("Emily")

'''
def add(x,y):
    z=x+y
    return z
add(3,6)
'''
def add(x,y):
    z=x+y
    return z
result = add(3,6)
print("the result of 3 + 6 =",result)