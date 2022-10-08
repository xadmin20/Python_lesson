# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:* # - 6 -> да # - 7 -> да # - 1 -> нет
def num_week():
    try:
        day = int(input('Введите номер дня недели: '))
        if 5 < day < 8:
            print('да')
        elif 0 < day < 6:
            print('нет')
        else:
            print('попробуй ввести от 1 до 7 включительно')
    except:
        print("Необходимо ввести номер дня недели!")
        num_week()


# num_week()

# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
def predicate():
    list_array = ["X", "Y", "Z"]
    arr = []
    for i in range(len(list_array)):
        arr.append(input(f"Введите значение {list_array[i]}: "))
    left = not (arr[0] or arr[1] or arr[2])
    right = not arr[0] and not arr[1] and not arr[2]
    if (not (arr[0] or arr[1] or arr[2])) == (not arr[0] and not arr[1] and not arr[2]):
        print(f"Утверждение истинно")
    else:
        print(f"Утверждение ложно")


# predicate()
# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
def coordinates():
    try:
        x, y = int(input("X: ")), int(input("Y: "))
        if x > 0 and y > 0:
            print("1")
        elif x < 0 and y > 0:
            print("2")
        elif x < 0 and y < 0:
            print("3")
        else:
            print("4")
    except:
        print("Введите пожалуйста целые числа!")
        coordinates()


coordinates()
