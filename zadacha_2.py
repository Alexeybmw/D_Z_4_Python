# Задайте натуральное число N. Напишите программу,которая составляет список простых множителей числа N.

num_n = int(input(f'Введите число: '))
mult = 2
list_mult = []
while num_n >= mult:
      if (num_n % mult) == 0:
            list_mult.append(mult)
            num_n /= mult
            mult = 2
      else:
            mult += 1
print(list_mult)