import pprint
import numpy
import scipy.linalg

B = numpy.array([[4, 6, 10], [6, 3, 19], [10, 19, 62]])
L = scipy.linalg.cholesky(B, lower=True)
U = scipy.linalg.cholesky(B, lower=False)

print("\nMATRIZ B\n")

print("B:")
pprint.pprint(B)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

