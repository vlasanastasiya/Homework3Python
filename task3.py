# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

list = [1.1, 1.2, 3.1, 5, 10.02]
min = 1
max = 0
for i in list:
        if (i - int(i)) <= min: min = i - int(i)
        if (i - int(i)) >= max: max = i - int(i)
find_max_min = max - min
print(math.floor(find_max_min*100)/100)