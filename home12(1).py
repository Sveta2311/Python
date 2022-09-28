# Реализуйте алгоритм перемешивания списка.
N = int (input('Bведите число > 0: '))
import random
list = []
if N > 0:
    for i in range(N):
        list.append(i)
    else:
        print(list)
        random_index = print(random.sample((list), N))
else:
    print("Ошибка ввода!")







    