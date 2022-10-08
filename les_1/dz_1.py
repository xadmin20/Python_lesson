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

# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
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


predicate()
