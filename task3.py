# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
textFirst = input('Введите первую строку: ')
textSecond = input('Введите вторую строку: ')



string = ''
subString = ''


if len(textFirst) > len(textSecond):
    string = textFirst
    subString = textSecond
else:
    string = textSecond
    subString = textFirst


print(string.count(subString))

