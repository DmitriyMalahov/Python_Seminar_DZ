# Задача 2: 
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input('Введите сколько журавликов дети сделали вместе: '))

p = int(s/6)
s = int(s/6)
k = int((p + s)*2)

print(f'Петя сделал {p} журавлика, Катя сделала {k}, а Серёжа {s}')