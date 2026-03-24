#MW_CP2 INHERITANCE

#inheritance:

#parent
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_vehicle(self):
        print(f"This is a {self.brand} {self.model}")

    def move(self):
        print("Vroom!")

class Car(Vehicle):
    pass

car = Car('Ford', 'Mustange')

car.show_vehicle()
car.move()