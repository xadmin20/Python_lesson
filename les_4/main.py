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

# print(num(input("Введите числа через пробел:\n").split(" ")))

# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random
def write_file(result):
    with open('f.txt', 'w', encoding="UTF-8") as data:
        data.write(result)
    print(result)


def create_random(k):
    l = [random.randint(0, 101) for i in range(k+1)]
    return l
def create_answ(sp):
    l = sp[::-1]
    res = ''
    if len(l)<1:
        res = 'x=0'
    else:
        for i in range(len(l)):
            if i != len(l)-1 and l[i]!=0 and i!=len(l)-2:
                res += f'{l[i]}x^{len(l)-i-1}'
                if l[i + 1] != 0:
                    res += ' + '
            elif i == len(l)-2 and l[i]!=0:
                res += f'{l[i]}x'
                if l[i + 1]!=0:
                    res += ' + '
            elif i == len(l)-1 and l[i]!=0:
                res += f'{l[i]} = 0'
            elif i == len(l)-1 and l[i]==0:
                res += ' = 0'
    return res
step = create_random(int(input("Введите натуральную степень k = ")))
write_file(create_answ(step))
print()