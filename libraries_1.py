from math import pow
from math import sqrt
from random import shuffle
from random import randint
from random import choice

result_1 = math.pow(2,4)
print("result 1 is", result_1)

result_2 = math.sqrt(16)
print("result 2 is", result_2)

result_3 = random.randint(0,100)
print("result 3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names", names)

random.shuffle(names)
print("Names after shuffling:", names)

result_4 = random.choice(names)
print("Chosen name is:", result_4)