"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Пример:
Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Текст после кодировки: 12W1B12W3B24W1B14W
Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""


def encoder():
    with open('file_054_1.txt') as text:
        input_text = list(text.read())
    encoded_text = ''
    n = 0
    for idx in range(1, len(input_text)):
        if input_text[idx] == input_text[idx - 1]:
            n += 1
        else:
            if n:
                encoded_text += f'{n + 1}{input_text[idx - 1]}'
                n = 0
            else:
                encoded_text += f'1{input_text[idx - 1]}'
    encoded_text += f'{n + 1}{input_text[-1]}'
    with open('file_054_2.txt', 'w') as cipher:
        cipher.write(encoded_text)


def decoder():
    with open('file_054_2.txt') as cipher:
        input_text = list(cipher.read())
    encoded_text = ''
    n = 0
    for i, sym in enumerate(input_text):
        if sym.isdigit():
            n += 1
        else:
            encoded_text += int(''.join(input_text[(i - n):i])) * sym
            n = 0
    with open('file_054_1.txt', 'w') as text:
        text.write(encoded_text)


# encoder()
decoder()
