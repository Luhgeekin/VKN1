a=int(input('введіть число: '))
b= a//10000
c = a%10
f = a % 10000 // 1000
g = a % 1000 // 100
print(b)
print(c)
result = b * c
result2 = f + g
print("Результат 1 = ",result)
print("Результат 2 = ",result2)
