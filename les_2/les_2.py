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

print(digit(int(input("Введите число: "))))
