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