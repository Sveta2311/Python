# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int (input('Bведите целое число > 0: '))
if n > 0:
    f = []
    a = 2
    m = n
    while a * a <= n:
        if n % a == 0:
            f.append(a)
            n//=a
            print(f)
        else:
            a += 1
    f.append(n)
    print('Список простых множителей {} = {}' .format(m, f))
    f = list(set(f))
    print(f)
else:
    print("Ошибка ввода!")