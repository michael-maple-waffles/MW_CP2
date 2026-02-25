#MW_CP2 Financial Calc

#Function for stupid proofing inside this there will be 2 parameters one will be 0, 1, or 2 (representing string int and float) and what the person inputed) (this will be called in every instance a person inputs something)
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

#function for finding a percentage this will have 2 parameteers the larger number (a float) and the percentage (an int) (this will allow for ease in compund interest, sales price, and tip calc)
def findPercent(total, peice):
    percent = total * (peice/100)
    return percent

#function for save for a goal
    #inside this function ask the user to input the goal ammount, how much they are putting in every time, and if its weekly or monthly.
def saving():
    goal = intInput(max = 1000000000000, prompt = "\nHow much money is the goal that you are saving for? ")
    often = intInput(prompt = "\nHow often in days are you paying (IE weekly would be 7)? ")
    amount_payed = intInput(max = goal, prompt = f"\nHow much are you paying every {often} days? ")
    
    div_goal = round(goal / amount_payed)

    time_to_pay = div_goal * often

    return [time_to_pay, goal]

#function for compound interest
    #this function will gt the users information of how much there payment was and what the interest was, it will then call the finding percent function
def compoundInterest():
    def compounding(start, times_compounded, percent_change):
        for i in range(times_compounded):
            start += findPercent(start, percent_change)
        
        return start

    starting = floatInput(max = 100000000000000000000000000000000000.00, prompt = "\nHow much did your money/payment start at? ")
    percent = floatInput(max = 1000.00, prompt = "\nWhat is the percent growth of this payment? (this is a percentage this number will be divided by 100) ", min = 0.00)

    time = intInput(max = 100000000000000000, prompt = "\nHow many times has this Compounded?")

    compounded = compounding(starting, time, percent)

    return [compounded, time]

#sales price and tip calc
def percentChange(total_prompt, peice_prompt, peice_max, value):
    total = floatInput(max = 1000000000000000000000000.00, prompt = total_prompt, min = 0.00)
    peice = floatInput(max = peice_max, prompt = peice_prompt, min = 0.00)

    change = findPercent(total, peice)
    if value == 0:
        changed = total - change
    elif value == 1:
        changed = total + change
    return [changed, change]

#function for budget allocator
    #this function will ask the user what there larger money portion is, how many goals there are and fill a dictionary.
def budget_allocator():
    #inner function for turning a percentage into a number
        #this will be used to turn the percent the person inputed into a number using the larger number they gave.
        

    total = floatInput(max = 1000000000000000000.00, prompt = "\nWhat is your total budget income?", min = 1.00)

    items_percents = {

    }
    percent_left = 100.00
    while True:
        choice = choiceInput(choices = ['1','2'], prompt = "\nPress '1' if you have an item that needs to be budgeted\nPress '2' if you are done\ninput here: ")
        if choice == '2':
            break
        elif choice == '1':
            item = input("\nWhat is the name of this item (example: rent)? ").strip().title()
            if item in items_percents.keys():
                print("\nYou have already used this name before!")
            elif percent_left == 0.00:
                print("You have no percent left.")
                break
            else:
                items_percents[item] = floatInput(max = percent_left, prompt = f"\nWhat percentage of your budget are you allocating to this?--NOTE you only have {percent_left} the number you input cant be greater than this number--(make this a integer bellow one hundred and above 0 IE: 23, or 10) ")
                percent_left -= items_percents[item]

    items_changed = {

    }

    for i in items_percents.keys():
        items_changed[i] = findPercent(total, items_percents[i])

    print("\n")

    for i in items_changed.keys():
        print(f"{i} : {items_changed[i]}$")
        

#Function to run everything
    #call everything, let them leave, let them navigate.
def mainMenu():
    while True:
        choice = choiceInput(choices = ["1","2","3","4","5","6"], prompt = "\nPress 1 if you would like to use the savings time calculator\nPress 2 if you would like to use the compound interest calculator\nPress 3 if you would like to use the budget allocator\nPress 4 if you would like to use the sales calculator\nPress 5 if you would like to use the tip calculator\nPress 6 if you would like to leave\nInput here: ")
        if choice == '6':
            break
        elif choice == '1':
            time = saving()
            print(f"\nIt will take you {time[0]} days to pay {time[1]}$\n")
        elif choice == '2':
            compounded = compoundInterest()
            print(f"\nAfter your item has compounded {compounded[1]} times it will be {compounded[0]}$")
        elif choice == '3':
            budget_allocator()
        elif choice == '4':
            changed = percentChange("\nWhat is the orginal price of the item? ", "What is it on sale for(this is a percentage and will be divided by 0 please make sure your number is bellow 100) ", 100, 0)
            print(f"Your Item now costs {changed[0]}$")
        elif choice == '5':
            changed = percentChange("\nHow much were you orginally paying? ", "What is your tip?(this is a percentage and will be divided by 0 please make sure your number is bellow 100) ", 100, 1)
            print(f"\nYour tip ammount is {changed[1]}$, your total is now {changed[0]}$")
        else:
            print("\nhow did you get here?")

mainMenu()