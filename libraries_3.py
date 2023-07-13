from math import pow as bow
from math import sqrt as bqrt
from random import randint as bandint
from random import shuffle as bhuffle
from random import choice as bhoice

result_1 = bow(2,4)
print("result 1 is", result_1)

result_2 = bqrt(16)
print("result 2 is", result_2)

result_3 = bandint(0,100)
print("result 3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names", names)

bhuffle(names)
print("Names after shuffling:", names)

result_4 = bhoice(names)
print("Chosen name is:", result_4)