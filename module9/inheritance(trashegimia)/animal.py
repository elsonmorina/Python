class Animal:
    def sound1(self):
        print("some generic animal sound")

class Dog(Animal):
    def sound2(self):
        print("woof! Woof")

class Cat(Animal):
    def sound3(self):
        print("mjau! mjau!")

animal = Animal()
animal.sound1()

dog = Dog()
dog.sound2()

cat = Cat()
cat.sound3()

dog = Dog()
dog.sound1()
