# Dhruvin Bhayani
# 105170206

listOfRanks=[]
rank1=0
rank2=0
print("RESULTS FOR MATCH FIXING\n")
openRanks = open('ranks.txt', 'r')
for line in openRanks:
    listOfRanks.append(line.strip())
matches = open('matches.txt', 'r')
for line in matches:
    lineStrip= line.strip()
    lineSplit=lineStrip.split(',')

    for i in range (0,len(listOfRanks),1):
        if(lineSplit[0]==listOfRanks[i]):
            rank1=i+1
        if(lineSplit[3]==listOfRanks[i]):
            rank2=i+1
    if(rank1>rank2):
        rankDif=rank1-rank2
    else:
        rankDif=rank2-rank1
    
    teambet1=int(lineSplit[2])
    teambet2=int(lineSplit[5])
    add=teambet1+teambet2
    if(rank1>rank2):
        div=teambet1/add
    else:
        div=teambet2/add
    if (rank2 >= 15 or rank1 >= 15) and (rankDif > 10 and div >0.8 and rank1>rank2):
                    print("%s\t%d\t%s\t%s\tvs\t%s\t%d\t%s\t%s" %(lineSplit[0],rank1,lineSplit[1],lineSplit[2],lineSplit[3],rank2,lineSplit[4],lineSplit[5]))
                elif(rank2>rank1):
                    print("%s\t%d\t%s\t%s\tvs\t%s\t%d\t%s\t%s" %(lineSplit[3],rank2,lineSplit[4],lineSplit[5],lineSplit[0],rank1,lineSplit[1],lineSplit[2]))