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


# print(f'Ответ: {sum(l)}')
##########################################
# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
l_1 = [2, 3, 4, 5, 6]
l_2 = [2, 3, 5, 6]

def mult_lst(lst):
    new_lst = []
    if len(lst) % 2 != 0:
        l = len(lst) // 2 + 1
    else:
        l = len(lst)//2
    for i in range(l):
        new_lst.append(lst[i]*lst[len(lst)-i-1])
    return new_lst


print(mult_lst(l_1))
print(mult_lst(l_2))