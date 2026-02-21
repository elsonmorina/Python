from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(7)
print(circle.area())

class Square(Shape):
    def __init__(self,brinja):
        self.brinja = brinja

    def area(self):
        return self.brinja * self.brinja
square = Square(25)
print(square.area())