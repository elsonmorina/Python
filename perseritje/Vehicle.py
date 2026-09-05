class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def __repr__(self):
        return f'Make:{self.make},Model:{self.model},Year:{self.year}'

class Car(Vehicle):
    def __init__(self,make,model,year,color):
        super().__init__(make,model,year)
        self.color=color

    def __repr__(self):
        return f"{super().__repr__()}, color: {self.color}"

class ElectricCar(Vehicle):
    def __init__(self,make,model,year,battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity=battery_capacity

    def battery_charging(self):
        print("Charging the electric car to:",self.battery_capacity,"km.")

    def __repr__(self):
        return f'This is an electric car:{super().__repr__()}.'

def main():
    tesla:ElectricCar=ElectricCar("tesla","X",2023,600)
    tesla.battery_charging()
    print(tesla)

if __name__=="__main__":
    main()