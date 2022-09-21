#14 варіант (1)
import math
x = float(input('введіть значення х: '))
print('f(x)= ', end="")
print(float(abs(math.sin(x) * 2 + math.cos(3*x + 1) + math.tan(abs(x) + 0.7)) + math.log10(abs(x-4))))