# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# k - максимальная степень многочлена, степень следующего на 1 меньше и так до ноля.
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени.
import random
k = int (input('Задайте степеь многочлена (введите целое число) > 0: '))
if k > 0:
    my_string = ""
    while k >= 0:
        r = random.randint(0,100)
        symbol_random = random.randint(0,10)
        symbol = " + "
        if symbol_random%2 > 0:
            symbol = " - "
        if r>0:
            if k !=0:
                my_string += str(r) + "x^" + str(k) + symbol
            else:
                my_string += str(r)
        k = k-1
    else:
        my_string += " = 0"
        data = open (r"equation.txt", "w")
        data.write(my_string)
        data.close() 
else:
    print("Ошибка ввода!")