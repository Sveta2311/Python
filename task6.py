# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
string = ['asdfs4fhg', 'fds4wr', 'ewe45fgvsdg']
num = input("Введите число: ")


for element in string:
    if num in element:
        print("Присутствует")
        break
else:
    print("Отстутсвует")



