# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
def mnoz(n):
    if n <= 1:
        return "Задайте натуральное число больше 1!"
    else:
        i = 2 # первое простое число
        new_list = []
        n_main = n
        while i <= n:
            if n % i == 0:
                new_list.append(i)
                n //= i
                i = 2
            else:
                i += 1
        return f"Ответ: {n_main} ---> {new_list}"


# print(mnoz(int(input("Задайте натуральное число N: "))))

# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def num(l):
    l = list(map(int, l))
    print(f"Исходный список: {l}")
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return f"Список из неповторяющихся элементов: {new_list}"

print(num(input("Введите числа через пробел:\n").split(" ")))
