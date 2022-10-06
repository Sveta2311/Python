# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

file1 = open (r"numbers1.txt", "r")
file2 = open (r"numbers2.txt", "r")
data1 = file1.read()
data2 = file2.read()
file1.close()
file2.close()


data1 = data1.split()
data2 = data2.split()


data1new = []
data2new = []

for elem in range(len(data1) - 1):
    if elem != 0:
        if elem%2 != 0:
            data1new.append(data1[elem] + data1[elem + 1])
    else:
        data1new.append(data1[elem])  

for elem in range(len(data2) - 1):
    if elem != 0:
        if elem%2 != 0:
            data2new.append(data2[elem] + data2[elem + 1])
    else:
        data2new.append(data2[elem])       
data1new.pop()
data2new.pop()
print(data1new)
print(data2new)




file3 = open (r"numbers3.txt", "w")
file3.write("123")
file3.close()

