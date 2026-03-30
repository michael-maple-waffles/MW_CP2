#MW_CP2


import random
#class Pet has these values: name, animal, age, health, happiness, hunger, days_hungry, energy, sleeping, !!rating!!
def userInput(prompt = '> '):
    return input(prompt).lower().strip()

def intInput(max = 100000,prompt='> ',min = 0):
    while True:
        num = userInput(prompt)
        try:
            num = int(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')

def floatInput(max = 100000.00,prompt='> ',min = 0.00):
    while True:
        num = userInput(prompt)
        try:
            num = float(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')

def choiceInput(choices,prompt = '> '):
    while True:
        choice = userInput(prompt)
        if choice in choices:
            return choice
        else:
            print('\nPlease select a valid choice!')

class Pet:
    def __init__(self, name, species, age, health=100, happiness=50, hunger=100, level=0, energy=100):
        #declair self
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.happiness = happiness
        self.hunger = hunger
        self.level = level
        self.energy = energy    #function to decide happiness

    def healthTracker(self, reason = "hunger", amount=0):
        if reason == "hunger":
            if self.hunger >= 90:
                self.Health += 3
            elif self.hunger >= 75:
                self.Health += 1
            elif self.hunger <= 10:
                self.Health -= 5
            elif self.hunger <= 25:
                self.Health -= 2
            else:
                pass
        
        elif reason == "over worked":
            self.Health -= 2

        else:
            self.Health += amount

        if self.Health > 100:
            self.Health = 100
        elif self.Health < 0:
            self.Health = 0

    def happinessTracker(self, reason="hunger", amount=0):
        #happiness will be decreased based on  hunger and energy
        if reason == "hunger":
            if self.hunger >= 90:
                self.happiness += 10
            elif self.hunger >= 75:
                self.happiness += 5
            elif self.hunger <= 10:
                self.happiness -= 10
            elif self.hunger <= 25:
                self.happiness -= 5
            else:
                pass
        
        elif reason == "over worked":
            self.happiness -= 10

        else:
            self.happiness += amount

        if self.happiness > 100:
            self.happiness = 100
        elif self.happiness < 0:
            self.happiness = 0

    #function to display stats:
    def showStats(self):
        return f"{self.name} | Happiness is currently {self.happiness}/100 | Hunger is currently {self.hunger}/100 | Energy is currently {self.energy}/100"
    
    #function for play:
    def play(self):
        if self.level == 0:
            print("\nYour pet ran in circles!")
        elif self.level == 1:
            print(random.choice("\nYour pet ran in circles!", "\nYour pet did a barrel roll!"))
        elif self.level == 2:
            print(random.choice("\nYour pet ran in circles!", "\nYour pet did a barrel roll!", "\nYour pet did a back flip!"))
        elif self.level >=3:
            print(random.choice("\nYour pet ran in circles!", "\nYour pet did a barrel roll!", "\nYour pet did a back flip!", "\nYour pet behaved perfectly!"))
        self.happiness += 20
        self.energy -= 30
        self.happinessTracker()
        if self.energy < 20:
            print("\n your pet is over worked!")
            self.happinessTracker(reason = "over worked")
        elif self.energy <= 50:
            print(f"your pet is starting to feel tired! current energy = {self.energy}")

        if self.energy < 0:
            self. energy = 0

        self.hunger -= 10
        if self.hunger >100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0

        self.happinessTracker("NULL")
        
        

    #function to put pet to sleep
    def sleep(self):
        self.energy += 100
        if self.energy >100:
            self.energy = 100
        elif self.energy < 0:
            self.energy = 0

        self.hunger -= 10
        if self.hunger >100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0

    #function to feed pet
    def feed(self):
        choice = choiceInput(['1','2','3'], '\nPress 1 if you would like to give your pet Normal Chow (easy to eat good fuel)\nPress 2 if you would like to give your pet Hungy Chow (refills hunger greatly, is exhuasting to eat)\nPress 3 if you would like to give your pet Speed Chow (easy to eat, not filing)')
        if choice == '1':
            self.hunger += 50
            self.energy -= 20
        elif choice == '2':
            self.hunger += 75
            self.energy -= 30
        elif choice == '3':
            self.hunger += 25
            self.energy -= 10

        self.happinessTracker()

        if self.energy <= 20:
            print("\n Your pet is overworked!")
            self.happinessTracker(reason="over worked")
        if self.energy < 0:
            self.energy = 0
        if self.hunger > 100:
            self.hunger = 100        
    #str function that just shows the pets name, age, and animal
    def __str__(self):
        return f"{self.name}, is a {self.animal}, who is {self.age} years old"