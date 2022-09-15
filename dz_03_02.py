#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = input('Введите числа: ').split()
my_list = list(map(int, my_list))
print(my_list)

my_list_len = len(my_list)/2

if my_list_len % 2:
    for i in range(int(my_list_len) + 1):
        print(f"{my_list[i]} * {my_list[-(i + 1)]} = {my_list[i] * my_list[-(i + 1)]}")
else:
    for i in range(int(my_list_len)):
        print(f"{my_list[i]} * {my_list[-(i + 1)]} = {my_list[i] * my_list[-(i + 1)]}")
