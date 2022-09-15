#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

my_list = input('Введите числа: ').split()
my_list = list(map(float, my_list))
min = 1
max = 0

for i in my_list:
    sublist = ['0', str(i).split('.')[1]]
    num = float('.'.join(sublist))
    if num < min:
        min = num
    if num > max:
        max = num
print(f'{max} - {min} = {max - min}')
