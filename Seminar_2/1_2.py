# Задача №1:

# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# Пример:
# 5 -> 1 0 1 1 0
# Ответ: 2

coins = int(input('Введите количество монет: '))
coins_list = []
for i in range(coins):
    side = int(input('Введите 1 или 0 (где 1 орел, а 0 решка): '))
    coins_list.append(side)

heads_count = 0
tails_count = 0
for i in range(len(coins_list)):
    if coins_list[i] > 0:
        heads_count += 1
    else:
        tails_count += 1
print('Минимум надо перевернуть монет:',
      heads_count if heads_count < tails_count else tails_count)
