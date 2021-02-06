# Dhruvin Bhayani
# 105170206


peopleData = open('people.txt', 'r')

listHobbies = []

for line in peopleData:
    linebyline = line.strip()
    lineSplit = linebyline.split(',')

    if lineSplit[1] not in listHobbies:
        listHobbies.append(lineSplit[1])
    if lineSplit[2] not in listHobbies:
        listHobbies.append(lineSplit[2])
    if lineSplit[3] not in listHobbies:
        listHobbies.append(lineSplit[3])

for i in range(0,len(listHobbies),1):
    fl = listHobbies[i] + ".txt"
    f = open(fl, "w")
    f.close()

peopleData = open('people.txt', 'r')

for line in peopleData:
    linebyline = line.strip()
    lineSplit = linebyline.split(',')

    fl = open(lineSplit[1] + ".txt" , 'a')
    fl.write(lineSplit[0] + "\n")

    fl = open(lineSplit[2] + ".txt" , 'a')
    fl.write(lineSplit[0] + "\n")

    fl = open(lineSplit[3] + ".txt" , 'a')
    fl.write(lineSplit[0] + "\n")

peopleData.close()