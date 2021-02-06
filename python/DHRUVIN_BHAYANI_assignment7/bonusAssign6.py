# Dhruvin Bhayani
# 105170206

File =  open("cheaters.txt", 'r')
readFile = File.read()
splitFile = readFile.strip().split('\n')
print("Cheaters who copied from chegg are:- ")
for i in range (len(splitFile)):
    sumASCII = 0
    for j in range(len(splitFile[i])):
        if ((splitFile[i][j]>='a' and splitFile[i][j]<='z') or (splitFile[i][j]>='A' and splitFile[i][j]<='Z')):
            sumASCII = sumASCII + ord(splitFile[i][j])
    if sumASCII > 1200:
        print(sumASCII,splitFile[i])
