import numpy as np
import random

m = int(input("Введіть m: "))
n = int(input("Введіть n: "))

arr = np.zeros((m, n), dtype=int)
new_column = []
count_of_1 = 0

for i in arr:
    for j in range(len(i)):
        i[j] = random.randint(0, 1)
        if i[j] == 1:
            count_of_1 += 1
    
    if count_of_1 % 2 == 0:
        new_column.append([0])
    else:
        new_column.append([1])
    count_of_1 = 0

new_array = np.append(arr, new_column, axis=1)

print(arr)
print(new_array)