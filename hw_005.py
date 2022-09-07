"""
Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
"""

import math

first_point_x = int(input('Введите абциссу точки 1: '))
first_point_y = int(input('Введите ординату точки 1: '))
second_point_x = int(input('Введите абциссу точки 2: '))
second_point_y = int(input('Введите ординату точки 2: '))

print(f'Точка 1: ({first_point_x};{first_point_y})')
print(f'Точка 2: ({second_point_x};{second_point_y})')

side1 = abs(first_point_x - second_point_x)
side2 = abs(first_point_y - second_point_y)

print(f'Горизонтальная сторона равна {side1}')
print(f'Вертикальная сторона равна {side2}')

dist = round(abs(math.sqrt(side1 ** 2 + side2 ** 2)), 2)

print(f'Расстояние между точками - {dist}')
