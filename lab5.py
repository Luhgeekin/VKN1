import math 
x = float(input('введіть значення х: '))
if x >= 3.86:
    F = math.sqrt(2.25*x + x**2 + math.log10(x))
elif x > 1.54:
    F = pow(math.e,x) + ((12*x**2)-1)/(x + 9)
else :
    F = math.log(abs(x), math.e) - pow (x,x)

print('F = ',F)