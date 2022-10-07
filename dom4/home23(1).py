file1 = open (r"numbers1.txt", "r")
file2 = open (r"numbers2.txt", "r")
data1 = file1.read()
data2 = file2.read()
file1.close()
file2.close()


def readEquation():
    file1 = data1()
    eqation = {}

data1 = data1.replace(" + ", " +").replace(" - ", " -").split()[:-2]

for i in range(len(data1)):
    eqation = {}
    data1[i] = data1[i].replace("+", "").split("x^")
    eqation[int(data1[i][1])] = int(data1[i][0])

finalWord = {}

word1 = readEquation()
word2 = readEquation()


for i in range(max(len(word1), len(word2)), -1, -1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0)

print(finalWord)