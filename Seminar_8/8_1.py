# Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt. Фамилия, имя, отчестово,
# номер телефона - данные, которые должны находится в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной.

# 1. Вывод всех контактов
# 2. Поиск контактов
# 3. Добавить контакт (сразу сохранить)
# 4. Выход по требованию пользователя

my_file = 'phone_book.txt'


def print_all_contacts(file):
    with open(file, 'r', encoding='utf8') as data:
        for line in data:
            print(line)


def find_contact(file, find_element):
    with open(file, 'r', encoding='utf8') as data:
        for line in data:
            if find_element in line:
                print(line)


def add_contact(file, new_contact):
    with open(file, 'a', encoding='utf8') as data:
        data.write(new_contact + '\n')


def delete_contact(file, del_element):
    with open(file,"r+", encoding='utf8') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if del_element not in line:
                f.write(line)
        f.truncate()


def main_menu(numb):
    if numb == 1:
        print_all_contacts(my_file)
    elif numb == 2:
        find_element = input('Введите Имя, Фамилию либо номер телефона для поиска: ')
        find_contact(my_file, find_element)
    elif numb == 3:
        new_contact = input('Введите Имя, Фамилию и номер телефона через пробел: ')
        add_contact(my_file, new_contact)
    elif numb == 4:
        del_element = input('Введите Фамилию или Имя контакта который хотите удалить: ')
        delete_contact(my_file, del_element)


while True:
    numb = int(input('Введите:\n 1 - для печати всех контактов;\n 2 - для поиска контакта;\n\
 3 - для добавления нового контакта в справочник;\n 4 - для удаления контаткта;\n 5 - для выхода из программы:  '))
    main_menu(numb)
    if numb == 5:
        break


