# Считайте из файла список чисел. Напишите программу, которая найдет большее и меньшее число и запишет их в отдельны файл. В качестве символа-разделителя используйте пробел.
data = open (r"Python\file.txt", "r")
file = data.read().split(" ")
data.close()
print(file)

for i in range(len(file)):
    if file[i].isdigit:
        file[i] = int(file[i])
print(file) 
k = min(file)        
print(k)
l = max(file)
print(l)

data = open (r"Python\file2.txt", "w")
data.write(f'{k}\n')
data.write(f'{l}\n')
data.close()
