# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел. БЕЗ КАКИХ ЛИБО РАНДОМОВ
from datetime import datetime
import time

def Random_number (min, max):
    if abs(max) > abs (min):
        check = min - 1
        max_abs = max + 1
    else:
        check = max + 1
        max_abs = min - 1
    random_number = check
    while random_number < min or random_number > max:
        temp_number = (float(time.time()) * float(datetime.now().time().microsecond)) / 1000000
        sign = -1
        if int(temp_number) % 2 != 0:
            sign = 1
        temp_number = temp_number - int(temp_number)
        random_number = abs(max_abs) * temp_number * sign
        random_number = int(random_number)
        time.sleep(0.000001)
    return random_number


def CreateList (size, min, max):
    createList = []
    for i in range(size):
        createList.append(Random_number(min, max))
    return createList
