# Напишите программу, которая принимает на вход координаты точки (X и Y), причём, X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
X = float (input('Введите координату X: '))
Y = float (input('Введите координату Y: '))
if X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print("Первая четверть!")
    elif X < 0 and Y > 0:
        print("Вторая четверть!")
    elif X < 0 and Y < 0:
        print("Третья четверть!")
    elif X > 0 and Y < 0:
        print("Четвертая четверть!")
else:
    print("Начало координат (0,0), повторите ввод точки!")