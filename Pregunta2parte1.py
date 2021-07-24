import pprint
import numpy
import scipy.linalg

A = numpy.array([[4, 6, 10], [6, 25, 19], [10, 19, 62]])
L = scipy.linalg.cholesky(A, lower=True)
U = scipy.linalg.cholesky(A, lower=False)

print("\n MATRIZ A \n")

print("A:")
pprint.pprint(A)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)


