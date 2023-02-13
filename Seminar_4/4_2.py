# Задача 2

# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# 4
# 1 2 3 4

# 9

number_bushes = int(input('Введите количество кустов на грядке: '))

number_list_berries = []
sequence_number_bushes = 1

for number_input in range(number_bushes):
    bush = int(input(f'Введите число ягод на кусте {sequence_number_bushes}: '))
    number_list_berries.append(bush)
    sequence_number_bushes += 1

for i in range(len(number_list_berries)-1):
    if i == 0:
        i += 1
        sum = number_list_berries[0] + number_list_berries[1] + number_list_berries[2]
    if i == number_list_berries[number_bushes-1]:
        i -=1
        sum = number_list_berries[-1] + number_list_berries[-2] + number_list_berries[-3]
    if sum < number_list_berries[i] + number_list_berries[i-1] + number_list_berries[i+1]:
            sum = number_list_berries[i] + number_list_berries[i-1] + number_list_berries[i+1]
    # print(sum)
    # print(i)

print(sum)