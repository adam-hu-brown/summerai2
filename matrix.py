import numpy as np 

A = [[3,5],[2,4]]
B = [[1,2],[3,4]]
C = np.add(A,B)
print("Element-wise sum of A and B is: ")
print(C)

D = np.subtract(A,B)
print("\nElement-wise subtraction of A and B is: ")
print(D)

E = np.multiply(A,B)
print("\nElement-wise multiplication of A and B is: ")
print(E)

F = np.dot(A,B)
print("\nDot product of A and B is: ")
print(F)
