# Задача 3: 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

n = int(input('Введите шесть чисел номера билета: '))

number1 = n % 10
number2 = n // 10 % 10
number3 = n // 100 % 10
sum1 = number1 + number2 + number3

number4 = n // 1000 % 10
number5 = n // 10000 % 10
number6 = n // 100000 % 10
sum2 = number4 + number5 + number6

result = 'YES' if (sum1 == sum2) else 'NO'
print(result)