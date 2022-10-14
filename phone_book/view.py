def get_data_record():
    list_1 = ('Фамилия', 'Имя', 'Телефон', 'Описание')
    user_data = []
    for val in list_1:
        user_data.append(input(f'{val} пользователя: '))
    return user_data


def get_data_io():
    file = input('Введите полное имя файла: ')
    return file


def result(case):
    if case == 1:
        print(f'Данные пользователя успешно записаны')
    elif case == 2:
        print(f'Данные импортированы в телефонный справочник')
    elif case == 3:
        print(f'Данные экспортированы из телефонного справочника')


def menu():
    chosen = False
    print(
        'Добро пожаловать!\n'
        '1 - Добавить запись в тел книгу вручную\n'
        '2 - Импортировать данные из файла\n'
        '3 - Экспортировать данные в файл\n'
        # '4 - Найти запись в книге\n'
        # '5 - Вывести содержимое книги\n'
        )
    while not chosen:
        user_choice = input('Ваш выбор: ')
        if 1 <= int(user_choice) <= 3:
            chosen = True
            return int(user_choice)
        else:
            print('Введите число от 1 до 3!')


# def ext_error(ext):
#     print(f'Значение расширения файла указано неверно: {ext}!')
