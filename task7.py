# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
list = ['s54dg5sg', 'sdf45sfs564fsdfs', 'sf45sda56sa', 'a0sa546s879dfg']
number = int(input('введите искомое число: '))
count = False
for i in list:
    for j in i:
        if j.isdigit() == True:
            if int(j) == number:
                count = True
                break
if count == True:
    print ('Есть')
else:
    print('Нет')
