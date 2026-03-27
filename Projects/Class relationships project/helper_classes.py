#MW_CP2 Helper classes

import random
#class called game
class Game:
#init there will be a bunch of objects held in this class, this will be an aggregate relatoinship with the characters class
    pass
#This class needs a function to select a character, and deal damage to them/veiw there stats
    #def get character
        #ask what the name of the user's character is
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



#class called character (aggregate to Game| composition with CharacterClass)
class Character:
#init there will be a few values: 1. a compostition relationship with a class called character class 2a. a value called max-health 2b. a valued called current health 3. a value called defense 4. a value called damage.
    #health is decided by a random number decided by the character class, pluss another number decided by character class then modified by your level.
    #defense is purely decided by the character class class and your level
    #damage is also purely decided by the character class class an your level
    def __init__(self, name, character_description, characters_class, start_level):
        self.name = name
        self.character_description = character_description
        self.characters_class = CharacterClass(characters_class, start_level)

        
        if start_level > 1:
            get_level_modifier = 0
            for level in range(0,start_level-1):
                get_level_modifier += 1

            self.health = self.characters_class.mainStat('health') + sum(list(map(lambda _: self.characters_class.statBoost('health'), range(get_level_modifier))))
            self.defense = self.characters_class.mainStat('defense') + sum(list(map(lambda _: self.characters_class.statBoost('defense'), range(get_level_modifier))))
            self.damage = self.characters_class.mainStat('damage') + sum(list(map(lambda _: self.characters_class.statBoost('damage'), range(get_level_modifier))))

            self.level = start_level

        elif start_level == 1:
            self.health = self.characters_class.mainStat('health')
            self.defense = self.characters_class.mainStat('defense')
            self.damage = self.characters_class.mainStat('damage')

            self.level = start_level

        else:
            print("impossible.")
            self.health = self.characters_class.mainStat('health')
            self.defense = self.characters_class.mainStat('defense')
            self.damage = self.characters_class.mainStat('damage')
            self.level = start_level
#function called take damage (self, amount)
    #take in an ammount then subtract that by the self.defense
    #then subract self.health by the new ammount

#a function called level up
    #apply bonus to health to max health and current health
    #apply bonus to defense
    #apply bonus to damage
    #increase level by 1

#function called __str__
    #show "charactername, level, class, health, defense, and damage"


#Class character class: (composition with Character)
class CharacterClass:
#init there are values: 1. spec (can be sorcerer, fighter, and paladin) 2. an ammount called damage modifiers, this is decided based on what spec is, {sorcerer : {damage : ((6,20), (1,8)), defense : ((1,10), (1,4)), health : ((15,25), (1,6))},          fighter : {damage : ((5,15),(1,6)), defense : ((8,15), (1,6)), health : ((25,35), (1,8)}, paladin : { damage : ((1,10), (1,4)), defense : ((10,20), (1,8)), health : ((25,40), (1,10))} super init previous stats
    def __init__(self, spec, level):
        self.spec = spec
        self.level = level
        self.modifiers = {'sorcerer' : {'damage' : ((6,20), (1,8)), 'defense' : ((1,10), (1,4)), 'health' : ((15,25), (1,6))}, 'fighter' : {'damage' : ((5,15),(1,6)), 'defense' : ((8,15), (1,6)), 'health' : ((25,35), (1,8))}, 'paladin' : {'damage' : ((1,10), (1,4)), 'defense' : ((10,20), (1,8)), 'health' : ((25,40), (1,10))}}
#mainStat(stat, self):
    #return random.randint(self.modifier[self.spec][stat][0])
    def mainStat(self,stat):
        return random.randint(self.modifiers[self.characters_class][stat][0])
#statBoost(stat, self):
    #return random.randint(self.modifier[self.spec][stat][1])
    def statBoost(self, stat):
        return random.randint(self.modifiers[self.characters_class][stat][1])
#there will also be a combat function inside this class

#combat(self):
#if self.spec == "sorcerer":


#class attack:
#init there are these variables: name of spell/ability, explanation of spell/ability, ammount it does(positive if heal negative if damage [SHOULD BE A TUPLE WITH 2 VALUES]), crit chance (if any), Super init 

#def use(self)
    #return value (along with any crit factor)

#def __str__:
    #return f"{self.name}, {self.explenation}"