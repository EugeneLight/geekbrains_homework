#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
fib_list = [0, 1]
rev_fib_list = fib_list.copy()
for i in range(n - 1):
    fib_list.append(fib_list[i] + fib_list[i + 1])
    rev_fib_list.append(rev_fib_list[i] - rev_fib_list[i + 1])
print(f'Правая часть: {fib_list}')
print(f'Левая часть: {rev_fib_list}')
final_list = list(reversed(rev_fib_list))
fib_list.remove(0)
final_list.extend(fib_list)
print(final_list)
