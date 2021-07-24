#DESCOMPOSICIÓN LU

import pprint
import scipy.linalg
import numpy


A = numpy.array([[6, 0, 0, 0], [3, 6, 0, 0], [4, -2, 7, 0], [5, -3, 9, 21]])
P, L, U = scipy.linalg.lu(A)

print("\nDESCOMPOSICIÓN LU\n")

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("Matriz U:")
pprint.pprint(U)

