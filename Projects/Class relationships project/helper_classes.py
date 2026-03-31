#MW_CP2 Helper classes

import random
#class called game

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


class Game:
#init there will be a bunch of objects held in this class, this will be an aggregate relatoinship with the characters class
    def __init__(self, name):
        self.name = name
        self.characters = {}
#This class needs a function to select a character, and deal damage to them/veiw there stats
    def create_character(self):
        print("\nYou have selected to make a character")
        while True:
            name = input("\tPlease enter the name of your character: ").strip().title()
            if name in self.characters:
                print("\n\nThat name already exists! please select a different one!")
            else:
                break
        
        char_class = choiceInput(['1','2','3'], "\n\tPress 1 if you would like to be a sorcerer (damage) \n\tPress 2 if you would like to be a fighter (balanced stats) \n\tPress 3 if you would like to be a paladin (health and armor) \n\tEnter Here: ")
        if char_class == '1':
            char_class = 'sorcerer'
        elif char_class == '2':
            char_class = 'fighter'
        elif char_class == '3':
            char_class = 'paladin'
        else:
            print("error code 1")
            char_class = "sorcerer"

        starting_level = intInput(max = 20, min = 1, prompt= "\n\tWhat is the level of your character? (1-20)\n\tEnter Here: ")
        new_char = Character(name,char_class,starting_level)
        print(new_char)
        self.characters[name] = new_char
        #def get character

    def get_character(self):

        choice = "maybe"

        print("\nGetting character")
        while True and choice != 'QUIT':
            for character in self.characters:
                print(character)
        #ask what the name of the user's character is
            queery = input("Please input one of the names listed above\n\tEnter Here: ").strip().title()
            if queery in self.characters:
                break
            else:
                print("\nThat isn't one of the characters!")
                while True:
                    choice = choiceInput(['1','2'], "\nWould you like to try again? If so press 1! If no Press 2!\n\tEnter Here: ")
                    if choice == '1':
                        break
                    elif choice == '2':
                        choice = "QUIT"
                        break

        if choice == 'QUIT':
            pass
        else:
            print(f"character gotten, {queery}")
            return queery

        #for character in self.characters
            #if inputted name == character.name
                #break
        #ask if they want to access this character
        #if yes, return character
        #elif no, ask if they want to try again
            #if yes, go back to begining
            #elif no, break
            #else, go back to previous question
        #else:
            #go back to previous question

    def showCharacters(self):
        for character in self.characters:
            print(self.characters[character].__str__())

    def battle(self):
        attendy_1 = self.get_character()
        choice = 'maybe'
        while True:
            attendy_2 = self.get_character()
            if attendy_2 == attendy_1:
                print("That is attendy 1!")
                choice = choiceInput(['1','2'], "\nPress 1 if you would like to try again\nPress 2 if you would like to quit!\n\tEnter Here: ")
                if choice == '1':
                    pass
                elif choice == '2':
                    choice = 'QUIT'
                    break
            else:
                break

        if choice == 'QUIT':
            pass
        else:
            attendy_1_health = self.characters[attendy_1].health
            attendy_2_health = self.characters[attendy_2].health
            while attendy_1_health > 0 and attendy_2_health > 0:
                attendy_2_health += self.characters[attendy_1].characters_class.combat()
                print(f"{attendy_1} attacked {attendy_2}, {attendy_2} now only has {attendy_2_health}")
                if attendy_2_health <= 0:
                    print(f"{attendy_1} has won")
                    break
                else:
                    attendy_1_health += self.characters[attendy_2].characters_class.combat()
                    print(f"{attendy_2} attacked {attendy_1}, {attendy_1} now only has {attendy_1_health}")
                    if attendy_1_health <= 0:
                        print(f"{attendy_2} has won!")




#class called character (aggregate to Game| composition with CharacterClass)
class Character:
#init there will be a few values: 1. a compostition relationship with a class called character class 2a. a value called max-health 2b. a valued called current health 3. a value called defense 4. a value called damage.
    #health is decided by a random number decided by the character class, pluss another number decided by character class then modified by your level.
    #defense is purely decided by the character class class and your level
    #damage is also purely decided by the character class class an your level
    def __init__(self, name, characters_class, start_level):
        self.name = name
        self.characters_class = CharacterClass(characters_class, start_level)

        
        if start_level > 1:
            get_level_modifier = 0
            for level in range(0,start_level-1):
                get_level_modifier += 1
            health = self.characters_class.mainStat('health') + sum(list(map(lambda _: self.characters_class.statBoost('health'), range(get_level_modifier))))
            self.health = health
            defense = self.characters_class.mainStat('defense') + sum(list(map(lambda _: self.characters_class.statBoost('defense'), range(get_level_modifier))))
            self.defense = defense
            damage = self.characters_class.mainStat('damage') + sum(list(map(lambda _: self.characters_class.statBoost('damage'), range(get_level_modifier))))
            self.damage = damage
            self.characters_class.dmg = damage
            self.characters_class.set_abilities()

            self.level = start_level

        elif start_level == 1:
            self.health = self.characters_class.mainStat('health')
            self.defense = self.characters_class.mainStat('defense')
            damage = self.characters_class.mainStat('damage')
            self.damage = damage
            
            self.characters_class.dmg = damage
            self.characters_class.set_abilities()

            self.level = start_level

        else:
            print("impossible.")
            self.health = self.characters_class.mainStat('health')
            self.defense = self.characters_class.mainStat('defense')
            damage = self.characters_class.mainStat('damage')
            self.damage = damage
            self.characters_class.dmg = damage
            self.characters_class.set_abilities()
            self.level = 1
#function called take damage (self, amount)
    #take in an ammount then subtract that by the self.defense
    #then subract self.health by the new ammount

#a function called level up
    def levelUp(self, amount):
    #apply bonus to health to max health and current health
        get_level_modifier = 0
        for level in range(0,amount):
            get_level_modifier += 1
        health_increase = sum(list(map(lambda _: self.characters_class.statBoost('health'), range(get_level_modifier))))
        self.health += health_increase
        defense_increase +=sum(list(map(lambda _: self.characters_class.statBoost('defense'), range(get_level_modifier))))
        self.defense = defense_increase
        damage_increase +=sum(list(map(lambda _: self.characters_class.statBoost('damage'), range(get_level_modifier))))
        self.damage = damage_increase
        self.characters_class.dmg += damage_increase

        self.level += amount
    #apply bonus to defense
    #apply bonus to damage
    #increase level by 1

#function called __str__
    #show "charactername, level, class, health, defense, and damage"
    def __str__(self):
        return f"{self.name}: Level : {self.level} | Health : {self.health} | Defense : {self.defense} | Damage : {self.damage}"


#Class character class: (composition with Character)
class CharacterClass:
#init there are values: 1. spec (can be sorcerer, fighter, and paladin) 2. an ammount called damage modifiers, this is decided based on what spec is, {sorcerer : {damage : ((6,20), (1,8)), defense : ((1,10), (1,4)), health : ((15,25), (1,6))},          fighter : {damage : ((5,15),(1,6)), defense : ((8,15), (1,6)), health : ((25,35), (1,8)}, paladin : { damage : ((1,10), (1,4)), defense : ((10,20), (1,8)), health : ((25,40), (1,10))} super init previous stats
    def __init__(self, spec, level, dmg = 0):
        self.spec = spec
        self.level = level
        self.dmg = dmg
        self.modifiers = {'sorcerer' : {'damage' : ((6,20), (1,8)), 'defense' : ((1,10), (1,4)), 'health' : ((15,25), (1,6))}, 'fighter' : {'damage' : ((5,15),(1,6)), 'defense' : ((8,15), (1,6)), 'health' : ((25,35), (1,8))}, 'paladin' : {'damage' : ((1,10), (1,4)), 'defense' : ((10,20), (1,8)), 'health' : ((25,40), (1,10))}}
        self.abilities = {'1' : Abilities("Big Damage", "Hit someone as hard as you can.", (-self.dmg,-self.dmg*2), 5, 2,0),'2' : Abilities("Heal", "Drink a potion IDK!", (self.dmg,self.dmg*2), 5, 2,0),'3' : Abilities("Lucky Shot", "deal no dmg, or all the dmg... your choice!!!", (self.dmg,self.dmg*2), 10, 2,0),}
#mainStat(stat, self):
    #return random.randint(self.modifier[self.spec][stat][0])
    def mainStat(self,stat):
        return random.randint(self.modifiers[self.spec][stat][0][0], self.modifiers[self.spec][stat][0][1])
#statBoost(stat, self):
    #return random.randint(self.modifier[self.spec][stat][1])
    def statBoost(self, stat):
        return random.randint(self.modifiers[self.spec][stat][1][0], self.modifiers[self.spec][stat][1][1])
#there will also be a combat function inside this class
    def set_abilities(self):
        self.abilities = {'1' : Abilities("Big Damage", "Hit someone as hard as you can.", (-self.dmg*2,-self.dmg), 5, 2,0),'2' : Abilities("Heal", "Drink a potion IDK!", (self.dmg,self.dmg*2), 5, 2,0),'3' : Abilities("Lucky Shot", "deal no dmg, or all the dmg... your choice!!!", (self.dmg,self.dmg*2), 10, 2,0),}

#combat(self):
    def combat(self):
        return self.abilities['1'].use()
#if self.spec == "sorcerer":


#class attack:
class Abilities:
#init there are these variables: name of spell/ability, explanation of spell/ability, ammount it does(positive if heal negative if damage [SHOULD BE A TUPLE WITH 2 VALUES]), crit chance (if any), Super init 
    def __init__(self, name, explanation, ammount, crit, crit_factor, lvl_access):
        self.name = name
        self.explanation = explanation
        self.amount = ammount
        self.crit_chance = crit
        self.crit_factor = crit_factor
        self.lvl_access = lvl_access
#def use(self)
    def use(self):
        print(self.amount)
        poss_crit = random.randint(1,100)
        if self.crit_chance >= poss_crit:
            crit = True
        else:
            crit = False

        strike = random.randint(self.amount[0], self.amount[1])
        print(strike)
        if crit == True:
            print(self.crit_factor)
            strike *= self.crit_factor
        else:
            pass

        return(strike)

    #return value (along with any crit factor)

#def __str__:
def __str__(self):
    return f"{self.name}: {self.explanation}"
    #return f"{self.name}, {self.explenation}"