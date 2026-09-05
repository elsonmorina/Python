

class Rectangle:
    def __init__(self,length,width:float):
        self.length=length
        self.width=width

    def __getattr__(self, item)->float|None:
        if item=="length":
            return self.length
        elif item=="width":
            return self.width
        else:
            print("No attribute corresponds to your item.")

    def calculate_area(self)->float:
        return self.width*self.length
    def calculate_perimeter(self)->float:
        return (self.width+self.length)*2

def main():
    r1:Rectangle=Rectangle(9.5,12)
    print(r1.calculate_area())

if __name__=="__main__":
    main()