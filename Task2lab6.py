from math import *

a = float(input("Введіть значення а: ")) 
b = float(input("Введіть значення b: ")) 
h = float(input("Введіть значення h: "))

x = a

while x <= b:

    y = round(exp(x) + sqrt(abs(x)), 4) 
    x = round(x, 4)

    print("x = " + str(x) + " - " + "y = " + str(y))
    
    x = x + h
