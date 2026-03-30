#MW_CP2 Menu and other functions put together
from pet_class import Pet, choiceInput, intInput,floatInput
import random
import csv


#function called create pet
def createPet(all_pets=[]):
#first ask what the pets name is, what species they are, and how old they are (in months)
    while True:
        name = input("\nWhat is the name of your pet?").title().strip()
        if name in all_pets:
            print("\nThat name is taken!")
        else:
            break
    species = input("\nWhat is the species of your pet?").title().strip()
    age = intInput(max = 100, min = 0, prompt = "\nHow old is your pet?")
    return (f'{name}',Pet(name, species, age))

#then return the information gathered, this should be set as "current pet"


def event(current_pet):
#function called event:
    #make a random choice between 4 events
    choice = random.randint(1,4)
    #choice one is your pet made a new friend +20 happiness and +10 health
    if choice == 1:
        print("\nYour pet met a new friend! (+20 happiness and +10 health)")
        current_pet.happiness += 20
        current_pet.health += 10
    #choice two is your pet got injured! -10 to health -20 to energy.
    elif choice == 2:
        print("\nYour pet got injured! (-10 health and -20 energy)")
        current_pet.health -=10
        current_pet.energy -= 20

    #choice three is your pet took an extra nap +30 energy
    elif choice == 3:
        print("\nYour pet took and extra nap! (+30 energy)")
        current_pet.energy += 30
    #choice four is pet found a small animal and ate it! + 25 to hunger, -2 to health
    elif choice == 4:
        print("\nYour pet ate a small animal!? (+25 to hunger and -2 to health)")

#function called save pet:
def save_pet(previous_data={}, new_data={}):
#get information to write,
#dict info = {}
    merged_dicts = previous_data | new_data
    dict_info = []
#for pet in pet dict:
    for pet in merged_dicts.keys():
        dict_info.append({"Name" : merged_dicts[pet].name, "Species" : merged_dicts[pet].species, "Age" : merged_dicts[pet].age, "Health" : merged_dicts[pet].health, "Happiness" : merged_dicts[pet].happiness, "Hunger" : merged_dicts[pet].hunger, "Energy":merged_dicts[pet].energy})
#dict_info.append{Name : current_pet.name, species : current_pet.species, Age : current_pet.age, health : current_pet.health, Happiness : current_pet.happiness, Hunger : current_pet.hunger, Energy:current_pet.energy, sleeping : current_pet.sleeping}
#fieldnames = ["Name","Species","Age","Health","Happiness","Hunger","Energy","Sleeping"]
    fieldnames = ["Name","Species","Age","Health","Happiness","Hunger","Energy"]
    #with open Projects/Pet Sim/saved_pet.csv 'w' as saving pet:
    try:
        with open("Projects/Pet Sim/saved_pet.csv", 'w') as saving_pets:
    #saver = csv.dictwriter(saving_pet, fieldnames=fieldnames)
            saver = csv.DictWriter(saving_pets, fieldnames=fieldnames)
    #saver.writeheader
            saver.writeheader()
    #saver.writerows(dict_info)
            saver.writerows(dict_info)
    except:
        print("\n\noops file failed\n\n")
    else:
        print("\nFile accessed successfully")

#function called load pets:
def loadPets():
    #data = []
    data = []
    #sendable data = {}
    sendable_data = {}
    #with open Projects/Pet Sim/saved_pet.csv 'r' as loading pet:
    try:
        with open("Projects/Pet Sim/saved_pet.csv", 'r') as loading_pets:
        #reader = csv.DictReader(loading pet)
            reader = csv.DictReader(loading_pets)
        #for row in reader:
            for row in reader:
            #data.append row
                data.append(row)
    except:
        print("\n\noops file failed\n\n")
    else:
        print("\nFile accessed successfully")

    #current pet = 0
    current_pet = 0
    #for item in data:
    for item in data:
    #sendabledata[[currentpet]['Name']] = Pet(data[currentpet]['Name'], data[currentpet]['Species'], data[currentpet]['Age'],data[currentpet]['Health'],data[currentpet]['Happiness'],data[currentpet]['Hunger'],data[currentpet]['Energy'],data[currentpet]['Sleeping'])
        sendable_data[data[current_pet]['Name']] = Pet(data[current_pet]['Name'],data[current_pet]['Species'],int(data[current_pet]['Age']),int(data[current_pet]['Health']),int(data[current_pet]['Happiness']),int(data[current_pet]['Hunger']),int(data[current_pet]['Energy']))
    #currentpet +=1
        current_pet += 1
    #return()
    return sendable_data

#function called run:
def run():
    time = 0
    exp = 0
    current_pets = {}
    current_pet = ""
#while True
    while True:
#if user has a curent pet:
        if bool(current_pet) == True:
    #ask user if they would like to play with the pet, feed the pet, veiw the pets stats, put the pet to sleep, check pets status, manage pets, save game, or quit
            choice = choiceInput(['1','2','3','4','5','6','7','8'], f"\nYou currently have {current_pet} selected!\n Press 1 to feed pet\n Press 2 to play with pet\n Press 3 to let pet sleep\n Press 4 to veiw pets stats\n Press 5 manage pets\n Press 6 to load game (will delete any unsaved progress)\n Press 7 to save game (will delete any unloaded data), or Press 8 to quite: : ")
            if choice =='1':
                current_pets[current_pet].feed()
                time += 1
            elif choice == '2':
                current_pets[current_pet].play()
                time += 1
                exp += 1
            elif choice == '3':
                current_pets[current_pet].sleep()
                time += 1
            elif choice == '4':
                print(current_pets[current_pet].showStats())
            elif choice == '5':
                choice = choiceInput(['1','2','3'], "\nPress 1 to make a new pet\nPress 2 to select a different pet\nPress 3 to release pet\nPress 4 to exit: ")
                if choice == '1':
                    new_pet = createPet(current_pets.keys())
                    current_pets[new_pet[0]] = new_pet[1]
                elif choice == '2':
                    while True:
                        print("\nPlease type the exact name of one of these pets")
                        for pet in current_pets:
                            print(pet)
                        
                        pet_input = input("\nEnter Here: ").strip().title()
                        if pet_input in current_pets:
                            current_pet = pet_input
                            break
                        else:
                            print("\nThat is a invalid input")
                            leave = choiceInput(['1','2'], 'Press 1 if you would like to try again\nPress 2 if you would like to exit: ')
                            if leave == '1':
                                pass
                            elif leave == '2':
                                break
                            else:
                                print("error code 1")
            elif choice == '6':
                current_pets = loadPets()
                if current_pet not in current_pets.keys():
                    current_pet = ''
            elif choice == '7':
                save_pet(new_data=current_pets)
            elif choice == '8':
                break

            if current_pets[current_pet].health == 0 and current_pet != '':
                print("\n Your pet has died!!!")
                current_pets.pop(current_pet)
                current_pet = ''

            if time % 4 == 0 and time != 0 and current_pet != '':
                print("\n your pet has aged up!")
                current_pets[current_pet].age += 1

            if exp == 4 and current_pet != '':
                print("\nYour pet has leveled up!")
                current_pets[current_pet].level += 1



#elif user currently has a pet in pet library:
        elif bool(current_pet) == False and bool(current_pets) == True:
            choice = choiceInput(['1','2','3','4','5','6'], "\nYou currently don't have a pet selected!\n Press 1 to make a new pet\n Press 2 veiw all currently made pets\n Press 3 to select a pet\n Press 4 to load the current save file (will delete any currently unsaved pets)\n Press 5 to save your currently made pets\n or Press 6 to quite: ")
            if choice == '1':
                    new_pet = createPet(current_pets.keys())
                    current_pets[new_pet[0]] = new_pet[1]
            elif choice == '2':
                for pet in current_pets:
                    print(pet)
            elif choice == '3':
                    while True:
                        print("\nPlease type the exact name of one of these pets")
                        for pet in current_pets:
                            print(pet)
                        
                        pet_input = input("\nEnter Here: ").strip().title()
                        if pet_input in current_pets:
                            current_pet = pet_input
                            break
                        else:
                            print("\nThat is a invalid input")
                            leave = choiceInput(['1','2'], 'Press 1 if you would like to try again\nPress 2 if you would like to exit: ')
                            if leave == '1':
                                pass
                            elif leave == '2':
                                break
                            else:
                                print("error code 1")
            elif choice == '4':
                current_pets = loadPets()
            elif choice == '5':
                save_pet(loadPets(), current_pets)
            elif choice == '6':
                break
            else:
                print("\nError code 1\n")
                    
                
                
    #show you don't currently have a pet picked!
    #show pets and in a way that the user can pick
    #allow the user to save.
    #allow the user to quit
#else:
        else:
    #ask the user if they would like to load game, make a new pet (overwriting save data), or quite
            choice = choiceInput(['1','2','3'], "Hello!\nwelcome to the pet simulator!\nPress 1 to make a new pet\nPress 2 to load the current save file\nor Press 3 to close out: ")
            if choice == '1':
                new_pet = createPet(current_pets)
                current_pets[new_pet[0]] = new_pet[1]
                current_pet = new_pet[0]
            elif choice == '2':
                current_pets = loadPets()
            elif choice == '3':
                break
            else:
                print("\nError code 1\n")

run()