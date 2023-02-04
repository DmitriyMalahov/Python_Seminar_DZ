# Задача №3:

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

num = int(input('Введите число N: '))

degree = 0
while 2**degree < num:
    num_degree = 2**degree
    degree += 1
    print(num_degree)