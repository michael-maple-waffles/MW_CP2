# MW_CP2 Classes notes

#example 1, dog

class Dog:
    def __init__(self, name, breed, age):
        self.name = name.title()
        self.breed = breed.title()
        self.age = age

    def __str__(self):
        return f" Name = {self.name}, Breed = {self.breed}, Age = {self.age}"
    
    def speak(self):
        return f'{self.name} said : "bark"'

doug = Dog('Doug', 'Golden Retriever', 3)
pongo = Dog('pongo', 'dalmation', 5)

print(doug)
print(doug.speak())
print(pongo)