"""
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.

Пример:
	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

A(x) = a
"""

import random

k = int(input('Введите число: '))
k_list = []
ratio = random.randint(0, 100)
multiplier = f'{ratio} = 0'

for i in range(k):
    ratio = random.randint(0, 100)
    if ratio != 0:
        if not i:
            multiplier = f'{ratio} * x + ' + multiplier
        else:
            multiplier = f'{ratio} * x ** {i + 1} + ' + multiplier

with open("file_045_2.txt", "w", encoding="utf-8") as result:
    result.write(multiplier)
print('Выполнено!')
