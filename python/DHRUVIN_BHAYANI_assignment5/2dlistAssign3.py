# Dhruvin Bhayani
# 105170206

import random
import math

total = 10     
empty = '_'
len = 30         
t = 'T'          
     
def Notplanted(yard, x, y): 
    for row in range(len):
      for col in range(len):
          if yard[row][col] == t:
              dist = math.sqrt((row-x)**2 + (col-y)**2)  
              if dist <= 3:
                  return True
    return False
    
treesTobePlanted = 0 
backList = [[empty for i in range(len)]for j in range(len)]   
for treesTobePlanted in range(total):
    x = random.randrange(0,len)
    y = random.randrange(0,len)
    if backList[x][y] == empty :
        if not Notplanted(backList, x, y): 
            backList[x][y] = t  
            treesTobePlanted = treesTobePlanted +1
for i in range(len):
    print(*backList[i])           



