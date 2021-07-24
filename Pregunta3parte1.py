#MÉTODO DE JACOBI

#Definiendo las ecuaciones a resolver
#en forma diagonalmente dominante

f1 = lambda w, x, y, z: (3 - x - y - 2*z)/7
f2 = lambda w, x, y, z: (-5 - w - 0*y + 2*z)/8
f3 = lambda w, x, y, z: (4 + w - 0*x + z)/4
f4 = lambda w, x, y, z: (-3 - 2*w + 2*x + y)/6

#Valores Iniciales
w0 = 0
x0 = 0
y0 = 0
z0 = 0
count = 1

#Error de Tolerancia
e = float(input('Enter tolerable error: '))

#Implementación de la Iteración de Jacobi
print('\nCount\tw\tx\ty\tz\n')

condition = True

while condition:
    w1 = f1(w0, x0, y0, z0)
    x1 = f2(w0, x0, y0, z0)
    y1 = f3(w0, x0, y0, z0)
    z1 = f4(w0, x0, y0, z0)

    print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' % (count, w1, x1, y1, z1))
    e1 = abs(w0 - w1);
    e2 = abs(x0 - x1);
    e3 = abs(y0 - y1);
    e4 = abs(z0 - z1);

    count += 1
    w0 = w1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e

print('\nSolución: w=%0.3f, x=%0.3f, y=%0.3f z=%0.3f\n' % (w1, x1, y1, z1))