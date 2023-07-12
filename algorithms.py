
def isintorfloat(num):
        try:
            float(num)
            return True
        except:
            return False
def task1():
    #Task 1

    #Checks if the inputted string is an int or a float
    

    num = input("How many hours do you want to convert?\n")
    #Catches when the user accidentally inputs a string
    while isintorfloat(num) != True:
        num = input("Sorry, that is not a number. Input again here:\n")
        if isintorfloat(num):
            break
    newnum = float(num)
    newnum *= 60
    print(str(num) + " hours is equivalent to " + str(newnum) + " minutes.")

def task2():
    #Task 2

    choice = input("If you want to convert hours to minutes, input H\nIf you want to convert minutes to hours, input M\n")

    #Catch if the user has not inputted H or M
    while choice != "M" and choice != "H" and choice != "m" and choice != "h":
        choice = input("Try again!\n")
        if choice == "M" or choice == "H":
            break
        

    if(choice == "M" or choice == "m"):
        num = input("How many minutes do you want to convert?\n")
        #Catches when the user accidentally inputs a string
        while isintorfloat(num) != True:
            num = input("Sorry, that is not a number. Input again here:\n")
            if isintorfloat(num):
                break
        newnum = float(num)
        newnum /= 60
        print(str(num) + " minutes is equivalent to " + str(newnum) + " hours.")
    if(choice == "H" or choice == "h"):
        num = input("How many hours do you want to convert?\n")
        #Catches when the user accidentally inputs a string
        while isintorfloat(num) != True:
            num = input("Sorry, that is not a number. Input again here:\n")
            if isintorfloat(num):
                break
        newnum = float(num)
        newnum *= 60
        print(str(num) + " hours is equivalent to " + str(newnum) + " minutes.")

def task3():
    #Task 3
    string = input("What is your word?\n")
    while str.isalpha(string) == False:
        string = input("Try again! That has numbers, spaces, or special characters in it!\n")
        if str.isalpha(string):
            break

    print("\"" + string + "\" " + "has " + str(len(string)) + " characters!")

replay = "y"
while replay != "n":
    task = input("Which task do you want to do?\nInput 1 for Task 1, 2 for Task 2, and 3 for Task 3!\n")
    while task != "3" and task != "2" and task != "1":
        task = input("Please try again!\n")
        if task == "3" or task == "2" or task == "1":
            break
    if task == "1":
        task1()
    if task == "2":
        task2()
    if task == "3":
        task3()
    print("\n\n\nThank you for playing!")
    replay = input("Would you like to play again? (y/n)\n")
    while replay != "y" and replay != "n":
        replay = input("I dont understand. Try again!\n")
        if replay == "y" or replay == "n":
            break
    if replay == "n":
        break