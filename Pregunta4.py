#NORMA DE FROBENIUS

from math import sqrt
row = 2
col = 2

#Función para devolver la norma de Frobenius
#Norma de la matriz dada

def frobeniusNorm(mat):
#Para almacenar la suma de cuadrados de los
#elementos de la matriz dada
	sumSq = 0
	for i in range(row):
		for j in range(col):
			sumSq += pow(mat[i][j], 2)

#Devuelve la raíz cuadrada de
#la suma de cuadrados
	res = sqrt(sumSq)
	return round(res, 5)

mat = [ [2, -3], [-1, 5] ]

print(frobeniusNorm(mat))

