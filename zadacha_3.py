# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


import random


num_n = int(input(f'Введите длинну списка: '))
list_num = []
for i in range(num_n):
      ran = random.randrange(0, 11)
      list_num.append(ran)
print(list_num)
print(set(list_num))