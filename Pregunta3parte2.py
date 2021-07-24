#MÉTODO DE GAUSS-SEIDEL

import numpy
m=int(input("\nValor de filas: "))
n=int(input("\nValor de columnas: "))
matrix = numpy.zeros((m,n))
x=numpy.zeros((m))

vector= numpy.zeros((n))
comp=numpy.zeros((m))
error=[]

print("\nMatriz y el vector solución\n")
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)] = float(input("Ingrese elemento a["+str(r+1)+","+str(c+1)+"]: "))
    vector[(r)] = float(input('\nb['+str(r+1)+']: '))
tol=float(input("\nTolerancia: "))
itera=int(input("\nNúmero de iteraciones: "))

k=0
while k<itera:
    suma=0
    k=k+1
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            if(c!=r):
                suma=suma+matrix[r,c]*x[c]
        x[r]=(vector[r]-suma)/matrix[r,r]
        print("x["+str(r)+"]: "+str(x[r]))
    del error[ : ]

    for r in range(0,m):
        suma=0
        for c in range(0,n):
            suma=suma+matrix[r,c]*x[c]
        comp[r]=suma
        dif=abs(comp[r]-vector[r])
        error.append(dif)
        print("Error en x[",r,"]= ",error[r])
    print("Iteraciones: ",k)
    if all ( i<=tol for i in error) ==True:
        break
print("Finalizado")