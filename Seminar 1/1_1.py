# Задача 1: 
# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите трехзначное число: '))

number3 = n % 10
number = n // 10
number2 = number % 10
number = number // 10
number1 = number % 10

print(f'Сумма цифр трехзначного числа {n} равна: {number1 + number2 + number3}')