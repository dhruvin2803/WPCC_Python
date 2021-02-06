# Dhruvin Bhayani
# 105170206

def empty(twoDlist):
    val = False 
    for row in range(len(twoDlist)):             
        for col in range(len(twoDlist[row])):   
          if twoDlist[row][col]==0:
            val = True                     
    return val   


def find (twoDlist, num):  
    x = 0         
    row = -1   
    col = -1   
    val = True
    if val == True:
        for x in range(len(twoDlist)):
            y = 0
            for y in range(len(twoDlist)):
                if(twoDlist[x][y] == num):
                    row = x
                    col = y 
                    val = False
                    break
                y = y + 1
            x = x + 1
        return [row , col]

# Main Code to test these functions
# grid = [[23, 34, 67], [44, 5, 3], [7, 8, 9]]
# print(empty(grid))
# print(find(grid, 34))

# grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(empty(grid))
# print(find(grid, 69))




