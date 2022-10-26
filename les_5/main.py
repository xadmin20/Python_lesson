# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""

from random import randint


def bot_game():
    bot_count = randint(1, 29)
    return bot_count


def input_dat(name):
    if name == "bot":
        x = bot_game()
        return x
    else:
        x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
        while x < 1 or x > 28:
            x = int(input(f"{name}, введите корректное количество конфет: "))
        return x


def game():
    player1 = input("Введите Ваше имя: ")
    player2 = input("Введите имя второго игрока или напишите 'bot' для игры с ботом: ")
    value = 2021
    counter1 = 0
    counter2 = 0
    turn = randint(0, 2)
    if turn:
        # color.BOLD + 'Hello World !' + color.END
        print(f"Первым ходит {player1}")
    else:
        print(f"Первым ходит {player2}")
    while value > 28:
        if turn:
            k = input_dat(player1)
            counter1 += k
            value -= k
            turn = False
            print(f"Ход {player1}, взял {k} конфет и теперь у него {counter1}. Осталось {value} конфет.")
            print("#" * 20)
        else:
            k = input_dat(player2)
            counter2 += k
            value -= k
            turn = True
            print(f"Ход {player2}, взял {k} конфет и теперь у него {counter2}. Осталось {value} конфет.")
            print("#" * 20)
    if turn:
        print(f"Выиграл: {player1}!")
    else:
        print(f"Выиграл: {player2}!")
# game()
# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 12W1B12W3B24W1B14W
file_code = "code.txt"
file_decode = "decode.txt"

# string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    with open(file_code, 'w', encoding="utf-8") as file:
        file.write(res)
    return res


def decoding():
    with open(file_code, "r", encoding="utf-8") as file_c:
        txt = file_c.read()
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    with open(file_decode, "w", encoding="UTF-8") as file:
        file.write(res)
    return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding()}")


# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

string = 'Доброе утро? как дела? абвгде все хорошо, а егдабв ты как?'
def find(string):
    abv = "абв"
    str_new = ''
    if abv in string:
        print(string.split(" "))
        for i in string.split(" "):
            if abv not in i:
                str_new = str_new + i + " "
    return str_new

print(find(string))


