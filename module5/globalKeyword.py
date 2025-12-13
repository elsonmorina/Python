

greeting = "Hello"
def greet(name):
    global message
    message = f"{greeting}, {name}"
    print(message)
greet("Bob")
print(message)
message = f"{greeting}, student"
print(message)