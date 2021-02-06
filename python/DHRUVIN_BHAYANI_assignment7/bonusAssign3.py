# Dhruvin Bhayani
# 105170206

import random

winList = ["Uruguay", "Italy", "Italy", "Uruguay", "West Germany", "Brazil", "Brazil","England", "Brazil", "West Germany", "Argentina", "Italy", "Argentina","West Germany", "Brazil", "France", "Brazil", "Italy", "Spain", "Germany","France"]
score = 0
year = 1930
options= []

for i in range(len(winList)):
    if winList[i] not in options:
        options.append(winList[i])
    else:
        pass

print(options)

randomyears = []
for i in range(21):
    randomyears.append(year)
    year = year + 4

for i in range(8):
    rnad = random.randint(0,20)
    print("Which team won in year ", randomyears[rnad])
    ans = winList[rnad]
    ansOption = random.randint(0,3)
    rand_options = []
    temp_options = options[:]
    temp_options.remove(ans)
    while len(rand_options)<3:
        temp = random.randint(0,len(temp_options)-1)
        if temp not in rand_options:
            rand_options.append(temp)
        else:pass
    temp = 0
    for i in range(4):
        if i == ansOption:print(i+1, ans)
        else: 
            print(i+1, options[rand_options[temp]])
            temp+=1

    userinput = int(input('Please enter your option.'))
    ansOption+=1
    if userinput == ansOption:
        print('correct ans', ans)
        score +=1
    else:
        print('wrong ans... correct answer is ', ansOption, '. ', ans)

finalscore = (score*100)/8 
if(finalscore>=90):
    print("you are genius... Final Score:- ", finalscore, "%")
elif(finalscore<90 and finalscore>=70):
    print("You have a pretty good knowledge.... Final Score:- ", finalscore, "%")
elif(finalscore>=30 and finalscore<70):
    print("you have average knowledege... Fianl Score:- ", finalscore, "%")
else:
    print("You have poor knowledge about this.... Final Score:- ", finalscore, "%")