#Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_list = input('Введите числа: ').split()
result = 0

for num in my_list[::2]:
    if not result:
        print(num, end='')
    else:
        print(f' + {num}', end='')
    result += int(num)
print(f' = {result}')
