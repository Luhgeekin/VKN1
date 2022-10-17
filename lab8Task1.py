from array import * 

m = array("i", [])
s = ""

for i in range(7):
    num = int(input("Введіть число: "))
    m.append(num)
    s += "Додатні дільники числа " + str(num) + ": "
    for j in range(1, abs(num) + 1):
        
        if num % j == 0:
            s += str(j) + " "
    s += "\n"

print(m)
print(s)