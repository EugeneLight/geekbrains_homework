"""
Напишите программу, удаляющую из текста все слова, содержащие "абв".
"""

text = input('Введите текст: ')

w_list = text.split()

for word in w_list:
    if 'абв' in word:
        w_list.remove(word)

print(' '.join(w_list))
