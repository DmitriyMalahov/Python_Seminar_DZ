# Задача 2.

# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# диапазон от 7 до 10

# Вывод: [1, 9, 13, 14, 19]


input_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# for number in input('Введите через пробел: ').split():
#     input_list.append( int(number) )
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

result_list = []
for i in range(len(input_list)):
    if min <= input_list[i] <= max:
        print(i)
