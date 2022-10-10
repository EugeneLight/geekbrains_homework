def heads_or_tails():
    op_list = list(input("Введите текст: "))
    count = 1
    ext_count = 1
    for i in range(1, len(op_list)):
        if op_list[i] == 'P' or op_list[i] == 'Р':
            if op_list[i] == op_list[i - 1]:
                count += 1
                if count > ext_count:
                    ext_count = count
            else:
                count = 1
    print(f'Наибольшее количество подряд выпавших Решек: {ext_count}')


heads_or_tails()
