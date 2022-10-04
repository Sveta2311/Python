pathRead = r"Python\text.txt"
pathWrite = r"Python\file4.txt"

try:
    with open (pathRead) as data:
        file = data.read().split(" ")
except:
    print("Файл не найден")

print(file)
listInt = []

for elem in file:
    if elem.isdigit():
        listInt.append(int(elem))

try:
    with open (pathWrite, 'w') as data:
        data.write(str(min(listInt)))
        data.write('\n')
        data.write(str(max(listInt)))
except:
    print("Ошибка работы с файлом")
