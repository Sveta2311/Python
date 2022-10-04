# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
import math

pathRead = r"Python\file1.txt"
pathWrite = r"Python\file3.txt"


try:
    with open (pathRead, 'r') as data:
        file = data.read().split(" ")
except:
    print("Файл не найден")

print(file)
coef = []

for elem in file:
    i =0
    #minicoef = ""
    try:
        while True:
            if elem[0+i].isdigit():
                #minicoef += elem[0+i]
                coef.append(elem[0+i])
                i += 1
            else:
                break
    except:
        pass

print(coef)

a = int(coef[0])
b = int(coef[1])
c = int(coef[2])

result = ''


discr = b**2 - 4*a*c
print(discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    result = f"x1 = {x1}\nx2 = {x2}"
elif discr == 0:
    x = -b / (2 * a)
    result = f"x1 = x2 = {x}"
else:
    result = "Корней нет"


try:
    with open (pathWrite, 'w') as data:
        data.write(result)

except:
    print("Ошибка работы с файлом")




