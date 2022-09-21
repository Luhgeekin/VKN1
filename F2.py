#14 варіант (2)
import math
x = float(input('введіть значення х: '))
y = float(input('введіть значення y: '))
def func(x,y):
    b = float(math.pow((x**2 + y**2), 1/3) + math.sin(x*3 + 1) + math.log(abs(x), math.e) - math.pow(math.e,(y-x)))
    return(b)
print('F = ', end="")
print(func(x,y))