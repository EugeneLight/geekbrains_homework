"""
Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.
"""

n = int(input('Введите число: '))
multipliers = []

for i in range(1, n):
    if n % i == 0:
        multipliers.append(i)
print(multipliers)
