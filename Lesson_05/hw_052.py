"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота "интеллектом"
"""

from random import randint


def candies_game(priority=2):
    candies = 2021
    if priority == 2:
        player = randint(0, 1)
    else:
        player = priority
    print(f'Первый ход делает Игрок {player + 1}')
    print('')

    while candies:
        grub = int(input(f'Сколько конфет возьмёте, Игрок {player + 1}? '))
        if grub > candies or grub > 28:
            print('Вы не можете взять так много!')
        else:
            candies -= grub
            player = not player
        print(f'Осталось {candies} конфет')
        print('*' * 16)
    player = not player
    print(f'Победил Игрок {player + 1}!')


def candies_game_with_bot(priority=2):
    candies = 2021
    if priority == 2:
        player = randint(0, 1)
    else:
        player = priority
    players = ['Бот', 'Игрок']
    print(f'Первый ход делает {players[player]}')
    print('')

    while candies:
        if player:
            grub = int(input(f'Сколько конфет возьмёте, {players[player]}? '))
            if grub > candies or grub > 28:
                print('Вы не можете взять так много!')
            else:
                candies -= grub
                player = not player
        else:
            grub = randint(1, 28)
            if grub >= candies or candies < 29:
                grub = candies
                candies -= grub
                print(f'Бот взял {grub} конфет')
                player = not player
            else:
                candies -= grub
                print(f'Бот взял {grub} конфет')
                player = not player
        print(f'Осталось {candies} конфет')
        print('*' * 16)
    player = not player
    print(f'Победил {players[player]}!')


candies_game()
# candies_game_with_bot()
