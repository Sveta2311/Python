# В текстовом файле на каждой строке стоит число. Нужно найти сумму элементов в списке, согласно числам в файле.
import random

number = int(input("Введите число: "))

listInt = []

for i in range(number):
    listInt.append(random.randint(-number, number))

print(listInt)

position = ''

with open('text.txt', 'r') as data:
    position = data.read().split('\n')

print(
    f'Произведение {int(position[0])} и {int(position[1])}'
    + f'элементов = {listInt[int(position[0])] * listInt[int(position[1])]}')
