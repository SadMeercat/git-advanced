# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def StepPlayer(candyes_count, max_value):
    global last_step
    player_inpt = int(input("Сколько конфет возьмем? "))
    while not (0 < player_inpt <= max_value):
        if(player_inpt <= 0):
            print("Нужно взять хотябы 1 конфету!")
            player_inpt = int(input("Сколько конфет возьмем? "))
        elif player_inpt > max_value:
            print(f"Ты слишко много на себя берешь... Максимум можно взять {max_value} конфет")
            player_inpt = int(input("Сколько конфет возьмем? "))
    else:
        if player_inpt > candyes_count:
            player_inpt = candyes_count
    last_step = player_inpt
    return candyes_count - player_inpt

def Calculate(candyes_count, max, last_round):
    value = max + 1 - last_round

    if candyes_count > max and (1 < candyes_count / max < 2):
        print(candyes_count - (max + 1))
        value = candyes_count - (max + 1) 
    if value > candyes_count or candyes_count <= max:
        value = candyes_count
    return value

candyes_count = 100
max_value = 28

player = randint(0,1)

print("Как играем? Против игрока или бота?\r\n 1. Игрок\r\n 2. Бот")
gamemode = int(input())

last_step = 0

while(candyes_count > 0):
    print(f"Ходит игрок {player + 1}")
    if player == 0: #типо игрок
        candyes_count = StepPlayer(candyes_count, max_value)
        if(candyes_count > 0):
            player += 1
    else:
        if gamemode == 1: # играет с игроком
            candyes_count = StepPlayer(candyes_count, max_value)
            if(candyes_count > 0):
                player -= 1
        else: # играет с ботом
            bot_inpt = Calculate(candyes_count, max_value, last_step)
            print(f"Бот взял {bot_inpt} конфет")
            candyes_count -= bot_inpt
            if(candyes_count > 0):
                player -= 1
    print(f"Осталось {candyes_count} конфет!\r\n_________________________")
else:
    print(f"Победа игрока {player + 1}!")