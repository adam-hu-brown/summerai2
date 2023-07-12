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
