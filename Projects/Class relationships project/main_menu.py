#MW_CP2 Main menu of character creator!

from helper_classes import Game, Character, CharacterClass, Abilities, choiceInput, intInput

def run_game():
    run = Game("Game 1")

    while True:
        if run.characters == {}:
            print("\nYou currently have no characters made!")

            choice = choiceInput(['1','2'], "\nPress 1 to make a character\nPress 2 to Exit!\n\tEnter Here: ")
            if choice == '2':
                break
            elif choice == '1':
                run.create_character()
            else:
                print("error code 1")

        elif bool(run.characters) == True and len(run.characters) > 1:
            choice = choiceInput(['1','2', '3','4','5'], "\nPress 1 to make a character\nPress 2 to Veiw characters\nPress 3 to level up a character\nPress 4 to battle two characters\nPress 5 to Exit!\n\tEnter Here: ")
            if choice == '5':
                break
            elif choice == '1':
                run.create_character()
            elif choice == '2':
                run.showCharacters()
            elif choice == '3':
                character = run.get_character()
                if run.characters[character].level == 20:
                    print("\nThis character is max level!")
                else:
                    maximum = 20-run.characters[character].level
                    amount_leveled = intInput(max = maximum, min= 1, prompt = "\nHow much are you leveling up your character?\n\tEnter Here: ")
                    run.characters[character].levelUp(amount_leveled)
            elif choice == '4':
                run.battle()

        elif bool(run.characters) == True:
            choice = choiceInput(['1','2', '3','4'], "\nPress 1 to make a character\nPress 2 to Veiw characters\nPress 3 to level up a character\nPress 4 to Exit!\n\tEnter Here: ")
            if choice == '4':
                break
            elif choice == '1':
                run.create_character()
            elif choice == '2':
                run.showCharacters()
            elif choice == '3':
                character = run.get_character()
                if run.characters[character].level == 20:
                    print("\nThis character is max level!")
                else:
                    maximum = 20-run.characters[character].level
                    amount_leveled = intInput(max = maximum, min= 1, prompt = "\nHow much are you leveling up your character?\n\tEnter Here: ")
                    run.characters[character].levelUp(amount_leveled)