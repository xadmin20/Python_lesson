# Задача 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
l = [2, 3, 5, 9, 3]


def sum(n):
    s = 0
    for i in range(len(n)):
        if i % 2 != 0:
            s = s + n[i]
    return s


print(f'Ответ: {sum(l)}')
##########################################
