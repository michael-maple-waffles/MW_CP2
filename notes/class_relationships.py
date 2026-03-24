#MW_CP2 INHERITANCE

#inheritance: (is a)

#parent
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_vehicle(self):
        print(f"This is a {self.brand} {self.model}")

    def move(self):
        print("Vroom!")
#composition
class Engine:
    def __init__(self, cylinders):
        self.cylinders = cylinders

    def __str__(self):
        return self.cylinders

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.engine = Engine("V8")

class Plane(Vehicle):
    def move(self):
        print("Flyyyy!")

class Boat(Vehicle):
    def move(self):
        print("sails!")

car = Car('Ford', 'Mustange')

boat = Boat("Boom Shock", "WireFine")

plane = Plane("Boeing", "747")


for x in (car, boat, plane):
    x.show_vehicle()
    x.move()

print(car.engine)
#aggregation (has a--> ONE WAY)
class Library:
    def __init__(self, name, catalogue = []):
        self.name = name
        self.catalogue = catalogue

    def addBook(self, book):
        self.catalogue.append(book)

    def removeBook(self, book):
        if book in self.catalogue:
            self.catalogue.pop(book)
        else:
            print("book doesn't exist")
    
    def veiwBook(self):
        for book in self.catalogue:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
lib = Library("provo library")

lib.addBook(Book("The Way of Kings", "Brandon Sanderson"))
lib.addBook(Book("The Words of Radiance", "Brandon Sanderson"))
lib.addBook(Book("Mistborn", "Brandon Sanderson"))

lib.veiwBook()


#composition (has a--> two way... they are dependant!