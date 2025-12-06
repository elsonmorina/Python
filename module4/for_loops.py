from traceback import print_tb

names = ["Alice","Bob","David","Charlie"]
for name in names:
    print(name)


sentence = "Hello, World!"
for ch in sentence:
    if ch.isalpha():
        print(ch)


for number in range(1,6):
    print(number)


numbers = [12,45,6,7,94]
max = numbers[0] #12
for num in numbers:
    if num > max:
        max = num #45
print('maksimumi eshte:', max)



count = 1
while count<=5:
    print("Rrite vleren per nje:" ,count)
    count+=1



numbers = [1,2,3,4,5,6]
target = 4
for number in numbers:
    print(number)
    if number == target:
        print("Target found")
        break



scores = [68, 42, 37, 55, 96, 74, 50]
total=0
count=0
for score in scores:
    if score<50:
        continue
    total+=score
    count+=1
mesatarja = total/count
print("Mesatarja eshte:", mesatarja)


# while True:
#     user_input = input("Shtyp nje numer pozitiv: ")
#     if user_input.isnumeric():
#         number = int(user_input)
#         if number > 0:
#             break
#     print("Invalid. Try again")
# print("You enter a pozotive number")

while True:
    user_input = input("Shtyp nje numer: ")
    if user_input.isnumeric():
        number = int(user_input)
        if number % 2==0:
            break
    print("numri esht tek")
print("numri esht qift")


