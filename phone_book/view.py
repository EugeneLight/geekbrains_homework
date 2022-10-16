def get_data_record():
    values_list = ('Фамилия', 'Имя', 'Телефон', 'Описание')
    user_data = []
    for val in values_list:
        user_data.append(input(f'{val} пользователя: '))
    return user_data


def get_data_io(case):
    result = ''
    if case == 2 or case == 3:
        result = input('Введите полное имя файла: ')
    elif case == 4:
        result = input('Введите искомое значение: ')
    return result


def result_message(case):
    if case == 1:
        print(f'Данные пользователя успешно записаны')
    elif case == 2:
        print(f'Данные импортированы в телефонный справочник')
    elif case == 3:
        print(f'Данные экспортированы из телефонного справочника')
    elif case == 4 or case == 5:
        pass


def menu():
    chosen = False
    print(
        'Добро пожаловать!\n'
        '1 - Добавить запись в тел книгу вручную\n'
        '2 - Импортировать данные из файла\n'
        '3 - Экспортировать данные в файл\n'
        '4 - Найти запись в книге\n'
        '5 - Вывести содержимое книги\n'
        '6 - Выход\n'
        )
    while not chosen:
        user_choice = input('Ваш выбор: ')
        if 1 <= int(user_choice) <= 6:
            chosen = True
            return int(user_choice)
        else:
            print('Введите число от 1 до 6!')


def show(data):
    print(f'\n{"#" * 3} Весь телефонный справочник {"#" * 3}\n')
    for value in data:
        print(value)


def show_search_result(result, query):
    print()
    if not result:
        print(f'Значение "{query}" не найдено!')
    else:
        for line in result:
            print(line)


# def ext_error(ext):
#     print(f'Значение расширения файла указано неверно: {ext}!')
