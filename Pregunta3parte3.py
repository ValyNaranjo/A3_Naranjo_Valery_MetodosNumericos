#MÉTODO SOR

import math
def column(m, c):
    return [m[i][c] for i in range(len(m))]

def row(m, r):
    return m[r][:]

def height(m):
    return len(m)

def width(m):
    return len(m[0])

def sor(m, w = 1.1, x0 = None, error = 1e-4, iteracion = 8):
    print("w =",w)
    print("\nError =", error)
    print("\nIteracion", iteracion)
    print(m)
    n = height(m)
    x0 = [0] * n if x0 == None else x0
    x1 = x0[:]
    for __ in range(iteracion):
        for i in range(n):
            s = sum(-m[i][j] * x1[j] for j in range(n) if i != j)
            x1[i] = round(w * (m[i][n] + s) / m[i][i] + (1 - w) * x0[i],4)
        if all(abs(x1[i] - x0[i]) < error for i in range(n)):
            return x1
        x0 = x1[:]
        print(x0)
    raise ValueError("La solución no converge")
m = [[7, 1, -1, 2,3],
    [1, 8, 0, -2,-5 ],
    [-1, 0, 4, -1,4 ],
    [2, -2, -1, 6,-3]]

print(sor(m))