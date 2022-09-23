import math
x = float(input('x = '))
y = float(input('y = '))
a = (x,y)

x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
b = (x2,y2)

x3 = float(input('x3 = '))
y3 = float(input('y3 = '))
c = (x3,y3)

print('A:',a)
print('B:',b)
print('C:',c)

def f1(a,b):
    rez = a + b
    return(rez)

def f2(a,b):
    rez = math.sqrt((a**2) + (b**2))
    return(rez)

A = f1(x,y)
B = f1(x2,y2)
C = f1(x3,y3)
A1 = f2(x,y)
B2 = f2(x2,y2)
C3 = f2(x3,y3)

if A < B and A < C:
    print('A min: ',A) 
    print('Відстань від точки A до початку кординат: ', A1)
elif B < A and B < C:
    print('B min: ',B)
    print('Відстань від точки B до початку кординат: ', B2)
elif C < A and C < B:
    print('C min: ',C)
    print('Відстань від точки A до початку кординат: ', C3)
else:
    print('введіть інші значення')