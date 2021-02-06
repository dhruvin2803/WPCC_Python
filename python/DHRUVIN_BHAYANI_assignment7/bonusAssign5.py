# Dhruvin Bhayani
# 105170206

def connect4(numbers):
    #for loop checks if there are any other numbers than 0,1 and 2
    for i in range(7):
        for j in range(7):
            if numbers[i][j] < 0 or numbers[i][j]>2: return False
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            currentNumber = numbers[i][j]
            if currentNumber == 1 or currentNumber == 2:
                #checks right side of the element
                if (j<=(len(numbers[i]))-4) and currentNumber == numbers[i][j+1] and currentNumber == numbers[i][j+2] and currentNumber == numbers[i][j+3] : return True
                #checks bottom of the element
                if (i<=(len(numbers))-4) and currentNumber == numbers[i+1][j] and currentNumber == numbers[i+2][j] and currentNumber == numbers[i+3][j] : return True
                #checks bottom right of the element
                if i<=((len(numbers))-3) and j<=((len(numbers[i]))-4):
                    if currentNumber == numbers[i+1][j+1] and currentNumber == numbers[i+2][j+2] and currentNumber == numbers[i+3][j+3]: return True
                #checks bottom left of the element
                if i<=((len(numbers))-4) and j>=((len(numbers[i]))-4): 
                    if currentNumber == numbers[i+1][j-1] and currentNumber == numbers[i+2][j-2] and currentNumber == numbers[i+3][j-3] : return True 
    return False
