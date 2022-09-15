#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите число: '))
bit_list = []

while num > 1:
    bit_list.append(str(num % 2))
    num = num // 2
bit_list.append(str(num))
print(''.join(bit_list)[::-1])
