# Задача 1

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# 11 6

# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

size_list_one = int(input('Введите длину первого множества: '))
number_list_one = []
sequence_number_one = 1

for number_input in range(size_list_one):
    number = int(input(f'Введите число {sequence_number_one}: '))
    number_list_one.append(number)
    sequence_number_one += 1

size_list_two = int(input('Введите длину второго множества: '))
number_list_two = []
sequence_number_two = 1

for number_input in range(size_list_two):
    number = int(input(f'Введите число {sequence_number_two}: '))
    number_list_two.append(number)
    sequence_number_two += 1

number_list_result = []
for i in range(size_list_one):
    for j in range(size_list_two):
        if number_list_one[i] == number_list_two[j]:
            number_list_result.append(number_list_one[i])

number_list_result_set = list(set(number_list_result))
print(f'Данные числа встречаются в обоих множествах: {sorted(number_list_result_set)}')