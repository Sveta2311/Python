# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int (input('Bведите число: '))
a = 1
for i in range(1, N + 1):
    a = a * i
    if i == N:
        print(a)
    else:
        print(a, end=', ')