# Создайте программу для игры в "Крестики-нолики".

"""
В скобках можно указать, кто будет ходить первым:
    0 - Нолики
    1 - Крестики
    2 - Случайный выбор
"""

from random import randint


def tic_tac_toe(first=2):
    field = {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
             (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
             (2, 0): ' ', (2, 1): ' ', (2, 2): ' '}
    players = {True: 'Крестики', False: 'Нолики'}
    if first == 2:
        player = randint(0, 1)
    else:
        player = first

    while True:
        if ' ' not in field.values():
            print('Ничья!')
            return
        else:
            print(f'Ход делают {players.get(player)}!')
            a = input('Введите через запятую координаты поля: ')
            if a == 'exit':
                return
            else:
                b = tuple(map(int, a.replace(' ', '').split(',')))
                if b in field.keys() and field.get(b) == ' ':
                    if player:
                        field[b] = 'X'
                    else:
                        field[b] = '0'
                    player = not player
                    print(f'|{field[(0, 0)]}|{field[(0, 1)]}|{field[(0, 2)]}|')
                    print(f'|{field[(1, 0)]}|{field[(1, 1)]}|{field[(1, 2)]}|')
                    print(f'|{field[(2, 0)]}|{field[(2, 1)]}|{field[(2, 2)]}|')
                    if field[(0, 0)] == field[(0, 1)] == field[(0, 2)] == 'X'\
                            or field[(1, 0)] == field[(1, 1)] == field[(1, 2)] == 'X'\
                            or field[(2, 0)] == field[(2, 1)] == field[(2, 2)] == 'X'\
                            or field[(0, 0)] == field[(1, 0)] == field[(2, 0)] == 'X'\
                            or field[(0, 1)] == field[(1, 1)] == field[(2, 1)] == 'X'\
                            or field[(0, 2)] == field[(1, 2)] == field[(2, 2)] == 'X'\
                            or field[(0, 0)] == field[(1, 1)] == field[(2, 2)] == 'X'\
                            or field[(0, 2)] == field[(1, 1)] == field[(2, 0)] == 'X'\
                            or field[(0, 0)] == field[(0, 1)] == field[(0, 2)] == '0'\
                            or field[(1, 0)] == field[(1, 1)] == field[(1, 2)] == '0'\
                            or field[(2, 0)] == field[(2, 1)] == field[(2, 2)] == '0'\
                            or field[(0, 0)] == field[(1, 0)] == field[(2, 0)] == '0'\
                            or field[(0, 1)] == field[(1, 1)] == field[(2, 1)] == '0'\
                            or field[(0, 2)] == field[(1, 2)] == field[(2, 2)] == '0'\
                            or field[(0, 0)] == field[(1, 1)] == field[(2, 2)] == '0'\
                            or field[(0, 2)] == field[(1, 1)] == field[(2, 0)] == '0':
                        player = not player
                        print(f'Победили {players.get(player)}!')
                        return
                elif field.get(b) != ' ':
                    print('Данная клетка уже занята!')
                else:
                    print('Данные указаны неверно! ', end='')


tic_tac_toe()
