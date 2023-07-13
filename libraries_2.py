import math as bath
import random as bandom

result_1 = bath.pow(2,4)
print("result 1 is", result_1)

result_2 = bath.sqrt(16)
print("result 2 is", result_2)

result_3 = bandom.randint(0,100)
print("result 3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names", names)

bandom.shuffle(names)
print("Names after shuffling:", names)

result_4 = bandom.choice(names)
print("Chosen name is:", result_4)