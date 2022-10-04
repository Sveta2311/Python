# Вычислить число pi c заданной точностью *d*.
import decimal
d =  decimal.Decimal(input('Введите дробное число в диапазоне от 0.1 до 0.0000000001: '))
if 0.1 >= d >= 0.0000000001:
    s = str(d)
    print(s)
    n = abs(s.find('.') - len(s))-1
    print(int(n))
    h = int(n)
    k = 1
    x = 0
    import random
    for k in range(1, 1000000):
        x = x+4*((-1)**(k+1))/(2*k-1)
    print(round(x,h))
else:
    print("Ошибка ввода, введите дробное число в диапазоне от 0.1 до 0.0000000001!")
