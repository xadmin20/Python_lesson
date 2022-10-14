# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и
# показывает сумму его цифр. Через строку нельзя решать.

# - 6782 -> 23
# - 0,56 -> 11
def suma(n):
    s = 0

    for i in n:
        if i.isdigit():
            s += int(i)
    return f"{n} -> {s}"

# print(suma(input("Введите число: ")))

def digit(n):
    s = 1
    l = []
    for i in range(1, n+1):
        s=s*i
        l.append(s)
    return l

# print(digit(int(input("Введите число: "))))


# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой. 
# COUNT или FIND нельзя юзать! говорил же на семинаре.

def count_to_str():
    a = str(input("A: "))
    b = str(input("B: "))
    count = 0
    answ = ''
    if len(a) >= len(b):
        for i in range(len(a)):
            if a[i] in b:
                answ = " ".join(a[i])
                count += 1
    else:
        for j in range(len(b)):
            if b[j] in a:
                answ = " ".join((b[j]))
                count += 1

    return f'Вхождений: {count}'

# print(count_to_str())
