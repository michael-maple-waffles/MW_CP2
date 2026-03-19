#MW_CP2

#class Pet has these values: name, animal, age, health, happiness, hunger, days_hungry, energy, sleeping, !!rating!!
class Pet:
    def __init__(self, name, animal, age, happiness, hunger, energy, sleeping):
        #declair self
        self.name = name
        self.animal = animal
        self.age = age
        self.happiness = happiness
        self.hunger = hunger
        self.energy = energy
        self.sleeping = sleeping
    #function to decide happiness 
    def happinessTracker(self):
        #happiness will be decreased based on  hunger and energy
        if self.hunger >= 90:
            self.happiness += 10
        elif self.hunger >= 75:
            self.happiness += 5
        elif self.hunger <= 10:
            self.happiness -= 10
        elif self.hunger <= 25:
            self.happiness -= 5

    def happinessChange(self, change=0):
        self.happiness += change

    #function to show pets current stats
    def showStats(self):
        

    #function to put pet to sleep

    #function to feed pet