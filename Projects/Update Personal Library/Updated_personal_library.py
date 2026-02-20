#MW_CP2 updated Personal library

#library information will be held in a list of tuples example: library = [(book, author)]
import csv

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
def showLibrary():
    try:
        with open("Projects/Update Personal Library/library.csv", mode = 'r') as library:
            reader = csv.reader(library)

            items = []
            for line in reader:
                items.append(f"{line[0]}|\t{line[1]}|\t{line[2]}|\t{line[3]}")
    except:
        print("file does not exist")
    else:
        for item in items:
            print(item)


#A function that allows you to add a book, this will be don by first asking the title of the book, and then asking for the author, the function will then return (book, author) as a tuple!
def addBook(library):
        title = input("\nWhat is the Title of your new book? ").title().strip()
        author = input("\nWho is the author of this book? ").title().strip()
        return (title,author)
            
#A function to search for a book: they will be given choice to search by author or book name: this will use the 'in' feature to check if the name of the author is in the string--or the name of the book if the user so picked to check  by name of book instead of author.
def searchForBook(by):
    if by == 'title':
        mode = 0
    elif by == 'author':
        mode = 1
    elif by == 'year':
        mode = 2
    elif by == 'genre':
        mode = 3

    def  searching(mode):
        try:
            with open("Projects/Update Personal Library/library.csv", mode = 'r') as library:
                reader = csv.reader(library)
                header = next(reader)
                possible_books = []
                base = []
                for line in reader:
                    possible_books.append(line)
                    base.append(line[by])
        except:
            print("this file does not exist")
        else:
            book_options = [possible_books, base]
            return book_options
    
    books = searching(mode)

    matches = []
    
    print(f"\nYou are currently searching by {by}")
    search = input("Input your search here: ").strip().lower()
    for book in books[1]:
        if search in book:
            index = book.index(books[1])
            matches.append(books[0][index])
        else:
            pass
    
    if matches != []:
        return
    



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

showLibrary()