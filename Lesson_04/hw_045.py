"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""

with open("file_045_1.txt") as first:
    list_m1 = first.read().split(' + ')

with open("file_045_2.txt") as second:
    list_m2 = second.read().split(' + ')

lst1 = []
lst2 = []
lst3 = []

for pie in list_m1:
    lst1.extend(pie.split(' * '))

for i in lst1:
    if 'x' not in i:
        if '=' in i:
            lst2.append(i.split(' = ')[0])
        else:
            lst2.append(i)

lst1 = []

for pie in list_m2:
    lst1.extend(pie.split(' * '))
for i in lst1:
    if 'x' not in i:
        if '=' in i:
            lst3.append(i.split(' = ')[0])
        else:
            lst3.append(i)

lst1 = []
result = ''

if len(lst2) == len(lst3):
    for idx in range(len(lst2)):
        lst1.append(int(lst2[idx]) + int(lst3[idx]))
for i, val in enumerate(lst1):
    result += f'{val} * x ** {len(lst1) - (i + 1)} + '
with open('file_045_3.txt', 'a') as res:
    res.write(result.replace('* x ** 0 +', '= 0').replace(' ** 1', ''))
print('Файл записан')
