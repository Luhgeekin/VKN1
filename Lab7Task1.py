s = input("Введіть строку: ").replace(" ", "").split(",")

s2 = str(s[0]) + ", " + str(s[-1])
print(s2)