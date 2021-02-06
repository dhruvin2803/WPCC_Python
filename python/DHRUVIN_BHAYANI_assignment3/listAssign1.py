# Dhruvin Bhayani
# 105170206

marks = []
topMarks = []
totalMarks = 0

#input of list from user
while True:
    inp = float(input("Enter the marks(press -1 to exit): "))
    if inp == -1:
        break
    marks.append(inp)

#finding top 6 marks 
for i in range(0, 6):
    maxValue = 0
    
    for j in range(len(marks)):
        if marks[j]>maxValue:
            maxValue = marks[j]

    marks.remove(maxValue)
    topMarks.append(maxValue) 

#finding average and median of list
for x in range(len(topMarks)):
    totalMarks = totalMarks + topMarks[x]
avg = totalMarks / len(topMarks)

#finding median
l = len(topMarks)
topMarks.sort()

if l % 2 == 0:
    median1 = topMarks[l//2]
    median2 = topMarks[l//2 - 1]
    finalMedian = (median1 + median2)/2

else:
    finalMedian = topMarks[l//2]

print("Top six Marks:- ")
print(topMarks)
print("Average of top 6 marks:- ",avg)
print("Median of Top 6 marks:- ", finalMedian)
