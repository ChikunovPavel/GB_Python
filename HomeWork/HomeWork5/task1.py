# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)
from random import randint

candy = 120
took = 28
easy  = 1   
hard = 2
player = 3
selest = int(input("select difficulty \n 1 - Easy bot \n 2 - Hard bot \n 3 - Players  \n:"))


while candy > 0:
    human = int(input("input candys took a human: "))
    if human > took:
        print(f'max took:{took}')
        human 
    elif candy < human:
        print(f'max candy:{candy}')
        human
    else:
        candy -= human
        print(f'candy:{candy}')
        if candy == 0:
            print("Human WiNER!!!")   
            break


        if selest == player:
            player2 = int(input("input candys took a player: "))
            if player2 > took:
                print(f'max took:{took}')
                player2 
            elif candy < player2:
                print(f'max candy:{candy}')
                player2
            else:
                candy -= player2
                print(f'candy:{candy}')
                if candy == 0:
                    print("Player WiNER!!!")   
                    break


        if selest == easy:
            if candy > took:
                bot = int(randint(1,took))   
                print(f'candys took a bot:{bot}')
            if  candy <= took:
                bot = int(randint(1,candy))
                print(f'candys took a bot:{bot}')
            if bot <= candy:
                candy -= bot
                print(f'candy:{candy}')
            if candy == 0:
                print("Easy Bot WINER!!!")
                break


        if selest == hard:
            if candy > took:
                bot = int(randint(1,took))   
                print(f'candys took a bot:{bot}')
            if  candy <= took:
                bot = candy
                print(f'candys took a bot:{bot}')
            if bot <= candy:
                candy -= bot
                print(f'candy:{candy}')
            if candy == 0:
                print("Hard Bot WINER!!!")
                break
            
# Не думаю что это тот самый ИИ , но вариант 2 однозначно более логически играет чем 1 вариант.
# Буду благодарен за ссылку на информацию на эту тему.
# Пока то что есть в интернете в первых выдачах  сложно воспренимаеться и не понятно ни чего.
# Спасибо!  





