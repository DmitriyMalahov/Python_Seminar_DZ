# Задание №1.

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# Ввод:

# пара-ра-рам рам-пам-папам па-ра-па-да

# Вывод:

# Парам пам-пам


input_poems_list = []
for phrase in input('Введите фразы через пробел: ').lower().split():
    input_poems_list.append((phrase))

sum_list = [(lambda x: sum(1 for i in x if i in 'аеёиоуыэюя'))(item) for item in input_poems_list]

if len(set(sum_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')