# Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
N = int (input('Bведите число (размер списка) > 0: '))
if N > 0:
    import random
    list = []
    for i in range(N):
        list.append(i)
    random.shuffle(list)
    print(f"Сгенерированный список: {list}")
    if N == 1:
        print("В списке нет элементов, стоящих на нечетных позициях!")
    else:
        print("Элементы списка, стоящие на нечетной позиции: ")
    for i in range(1, len(list), 2):
            if i == N-1 or i == N-2:
                print(list[i])
            else:
                print(list[i], end=", ")
    else:
        print(f"Сумма элементов списка, стоящих на нечетной позиции: {sum(list[1::2])}") 
else:
    print("Ошибка ввода!")


 