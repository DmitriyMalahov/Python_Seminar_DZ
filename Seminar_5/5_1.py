# Задача 1

# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)

# A = 2; B = 3 -> 8

def degree_number(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 0
    else:
        return (a * degree_number(a,b-1))

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))

print(f'Число {a} в степени {b} равно: {degree_number(a,b)}')