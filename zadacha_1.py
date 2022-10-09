# Вычислить число с заданной точностью d


import math

num_n = int(input(f'Сколько цыфр должно остаться после зыпятой: '))
pi = round((math.pi), num_n)
print(f"{pi}")