# Задача 2

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# 2 2

# 4


sys.getrecursionlimit(15000)

def sum_two_numbers(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > 0:
        return sum_two_numbers(a-1,b+1)
    if b > 0:
        return sum_two_numbers(a+1,b-1)
    
a = int(input('Введите число а: ')) 
b = int(input('Введите число b: '))
print(sum_two_numbers(a, b))

