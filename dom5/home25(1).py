# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока, делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) добавьте игру против бота
# b) подумайте как наделить бота 'интеллектом'

from random import randint, choice

greeting = ('На столе лежит 150 конфет.\nИграют два игрока, делая ход друг после друга.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\nСколько конфет нужно взять первому игроку,\nчтобы забрать все конфеты у своего конкурента?')

def meeting_players():
    player1 = input('Первый игрок, как вас зовут:\n')
    player2 = 'Второй игрок!'
    print(f'{player2}')
    return [player1, player2]

def get_rules(players):
    n = 150
    m = 28
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу:\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]

def play_game(rules, players):
    count = 0
    count = rules[2]
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Второй игрок: Я забираю {move} конфет!')
        else:
            print(f'{players[0]}, возьмите конфеты:')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(f'Можно взять не более {rules[1]} конфет, у нас всего {rules[0]} конфет.')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет!')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]

print(greeting)

players = meeting_players()

rules = get_rules(players)

victory = play_game(rules, players)
if not victory:
    print('Нет победителя!')
else:
    print(f'Победил {victory}!')