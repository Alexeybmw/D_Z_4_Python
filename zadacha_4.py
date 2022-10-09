#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input("Введите число k: "))

koef_list = []
for i in range(k + 1):
      koef_list.append(random.randint(0, 100))
print(koef_list)
equation = ""
for j in range(k + 1):
      if j < k:
            equation += f'{koef_list[j]} x^ {k - j} + '
      else:
            equation += f'{koef_list[j]} x^ {k - j} = 0'

with open ('file_zadacha_4.txt', 'w') as data:
      data.write(equation)
data.close()