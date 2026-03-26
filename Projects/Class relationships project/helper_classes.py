#MW_CP2 Helper classes

#class called game

#init there will be a bunch of objects held in this class, this will be an aggregate relatoinship with the characters class

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

#init there will be a few values: 1. a compostition relationship with a class called character class 2a. a value called max-health 2b. a valued called current health 3. a value called defense 4. a value called damage.
    #health is decided by a random number decided by the character class, pluss another number decided by character class then modified by your level.
    #defense is purely decided by the character class class and your level
    #damage is also purely decided by the character class class an your level

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
#init there are values: 1. spec (can be sorcerer, fighter, and paladin) 2. an ammount called damage modifiers, this is decided based on what spec is, {sorc : ((6-20), (1-8), fighter : ((5-15),(1-6)), paladin : ((1-10), (1-4)}