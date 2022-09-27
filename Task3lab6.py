from math import *

a = float(input("Введіть значення а: ")) 
b = float(input("Введіть значення b: ")) 
h = float(input("Введіть значення h: "))

x = a
values = []

while x <= b:

    y = round(exp(x) + sqrt(abs(x)), 4) 
    x = round(x, 4) 

    values.append(y)
       
    x = x + h 

print(values)
min_values = []
n = 4

if n > len(values):
    n = len(values) 

for i in range(n):
    min_value = min(values)
    min_values.append(min_value)
    values.remove(min_value)

print("Мінімальні значення у - " + str(min_values))