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
            print('Input is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('Input is out of range!')

def floatInput(max = 100000.00,prompt='> ',min = 0.00):
    while True:
        num = userInput(prompt)
        try:
            num = float(num)
        except:
            print('Input is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('Input is out of range!')

def choiceInput(choices,prompt = '> '):
    while True:
        choice = userInput(prompt)
        if choice in choices:
            return choice
        else:
            print('Please select a valid choice!')

#function for finding a percentage this will have 2 parameteers the larger number (a float) and the percentage (an int) (this will allow for ease in compund interest, sales price, and tip calc)
def findPercent(total, peice):
    percent = total * (peice/100)
    return percent

#function for save for a goal
    #inside this function ask the user to input the goal ammount, how much they are putting in every time, and if its weekly or monthly.
def saving():
    runs = 0
    amount = "VOID"

    while stupidProof(1,amount, False) is False:
        if runs >= 1:
            print("make sure you are inputing a float number include the '.00'")
        amount = input("What is your goal amount?")

    runs = 0
    payments = "VOID"
    while stupidProof(2 ,payments, (1,5)) is False:
        if runs >= 1:
            print("make sure you are inputing a integer (a number)")

        payments = input("press 1 if you are making payments monthly, press 2 if you are making payments bi-weekly, press 3 if you are making payments weekly, press 4 if you are making payments every other day, and press 5 if you are making payments daily.")

    runs = 0
    number = "VOID"
    while stupidProof(2,number, False) is False:
        if runs >= 1:
            print("make sure you are inputing a integer (a number)")

        number = int(input("How much are you paying for each time?"))

    div = amount/number
    credited = {
            
     }
    
    if payments == "1":
        credited["months"] = div
        credited["weeks"] = div * 4
        credited["days"] = div *4 * 7
    elif payments == "2":
        credited["months"] = div / 2
        credited["weeks"] = div * 2
        credited["days"] = div * 7 * 2
    elif payments == "3":
        credited["months"] = div / 4
        credited["weeks"] = div
        credited["days"] = div * 7
    elif payments == "4":
        credited["months"] = div / 4
        credited["weeks"] = div
        credited["days"] = div * 7

#function for compound interest
    #this function will gt the users information of how much there payment was and what the interest was, it will then call the finding percent function
def compoundInterest():
    loan = floatInput(max = 1000000000000000000000000.00, prompt = "How much did you pay on this loan?", min = 0.00)
    percent_increase = floatInput(max = 1000.00, prompt = "Hwhat is the interest on this loan?", min = 0.00)

    growth = findPercent(loan, percent_increase)

    increased_percentage = loan + growth
    return increased_percentage

#function for budget allocator
    #this function will ask the user what there larger money portion is, how many goals there are and fill a dictionary.

    #inner function for turning a percentage into a number
        #this will be used to turn the percent the person inputed into a number using the larger number they gave.

#function for sales price
    #this function will ask for the item, and its sale, then it will call the finding percent function and subract from the larger portion

#function for tip calc
    #same thing as the last function, but it will insted add to it.

#Function to run everything
    #call everything, let them leave, let them navigate.