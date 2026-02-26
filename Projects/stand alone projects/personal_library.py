#MW_CP2 Personal library

#library information will be held in a list of tuples example: library = [(book, author)]
library = []
#imported functions for inputs/stupid proofing
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

#function that loops through the list to print every book and its author neatly
def showLibrary(library):
    if library == []:
        print("\nThere are no books in your library!\n")
    else:
        for book in library:
            print(f" Book: {book[0]} | By: {book[1]}")

#A function that allows you to add a book, this will be don by first asking the title of the book, and then asking for the author, the function will then return (book, author) as a tuple!
def addBook(library):
        title = input("\nWhat is the Title of your new book? ").title().strip()
        author = input("\nWho is the author of this book? ").title().strip()
        return (title,author)
            
#A function to search for a book: they will be given choice to search by author or book name: this will use the 'in' feature to check if the name of the author is in the string--or the name of the book if the user so picked to check  by name of book instead of author.
def searchForBook(library):

    def searching(library, by):
        done = ''
        if by == 'title':
            mode = 0
        elif by == 'author':
            mode = 1
        while True:
            options = 0
            search = input(f"\nYou are currently searching by {by}:\n    Search Here: ")

            for book in library:
                if search.lower() in book[mode].lower():
                    print(f"Book: {book[0]} | By: {book[1]}")
                    options += 1

                else: 
                    pass
            
            if options == 0:
                print(f"\nYou have no books with that set of words for its {by}\n")

            done = choiceInput(['y', 'n'], "\nWould you like to try searching again? (press 'y' if so, and 'n' if not so): ")
            if done == 'y' or '':
                pass
            elif done == 'n':
                break

    searching_by = choiceInput(['1', '2'], "\nPress '1' if you are seaching by title of book\n Press '2' if you are searching by author of book\nInput here: ")

    if searching_by == '1':
        searching(library, 'title')
    elif searching_by == '2':
        searching(library, 'author')

#A function to let them remove a book: we will try by searching and inputting the name... if it proves to difficult we will do it by listing all books as choices and letting the user pick one by number.
def removeBook(library):
    choices = {

    }

    option = 0

    phrase = f''

    for book in library:
        option += 1
        choices[str(option)] = book
        phrase = phrase + (f"\nPress {option} to remove {book[0]} from your library")

    removed = choiceInput(choices.keys(), prompt = f"{phrase}\n  Input Here: ")
    
    return choices[removed]

#main menu function.
def mainMenu(library):
    print("This program is ment to work as a personal library\n")

    while True:
        choice = choiceInput(['1','2','3','4','5'], "\n\nPress '1' if you would like to veiw your current library\nPress '2' if you would like to add a new book\nPress '3' if you would like to remove from your library\nPress '4' if you would like to search your library\nPress '5' if you would like to exit this program\n   Enter Here: ")

        if choice == '5':
            break
        
        elif choice == '1':
            showLibrary(library)

        elif choice == '2':
            library.append(addBook(library))

        elif choice == '3':
            if library != []:
                library.remove(removeBook(library))
            else:
                print("\nYou do not currently have any books to remove.\n")

        elif choice == '4':
            if library != []:
                searchForBook(library)
            else:
                print("\nYou do not currently have any books to search.\n")

mainMenu(library)