"""
Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
"""

day = int(input('Введите номер дня недели: '))

if 1 <= day <= 5:
    print('Нет')
elif 6 <= day <= 7:
    print('Да')
else:
    print('Введите число от 1 до 7')
