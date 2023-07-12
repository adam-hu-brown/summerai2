#Task 1

#Checks if the inputted string is an int or a float
def isintorfloat(num):
    try:
        float(num)
        return True
    except:
        return False

num = input("How many hours do you want to convert?\n")
#Catches when the user accidentally inputs a string
while isintorfloat(num) != True:
    num = input("Sorry, that is not a number. Input again here:\n")
    if isintorfloat(num):
        break
newnum = float(num)
newnum *= 60
print(str(num) + " hours is equivalent to " + str(newnum) + " minutes.")

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
