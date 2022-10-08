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


# coordinates()

# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
def calc():
    try:
        a = float(input('a: '))
        o = input("Поддерживаемые операции: +, -, /, *, mod, pow, div: ")
        b = float(input('b: '))
        if o == 'mod':
            print(a % b)
        elif o == 'pow':
            print(a ** b)
        elif o == 'div':
            print(a // b)
        elif o == '+':
            print(a + b)
        elif o == '-':
            print(a - b)
        elif o == '*':
            print(a * b)
        elif o == '/':
            if b == 0:
                print('Деление на 0!')
            else:
                print(a / b)
        else:
            print("Введите число или правильную операцию")
            calc()
    except:
        print("Введите число или правильную операцию")
        calc()


# calc()

# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10
def sorted_list():
    try:
        a = []
        for i in range(4):
            a.append(int(input("A: ")))
        b = []
        for i in range(4):
            b.append(int(input("B: ")))
        print(sorted(a))
        print(sorted(b))
    except:
        print("Введите числа")
        sorted_list()


# sorted_list()

def sorted_two():
    a = []
    b = []
    for i in range(4):
        a.append(int(input("A: ")))
    for i in range(4):
        b.append(int(input("B: ")))
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if b[i] > b[j]:
                b[i], b[j] = b[j], b[i]

    print(a)
    print(b)

sorted_two()
