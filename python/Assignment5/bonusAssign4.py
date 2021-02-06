# Dhruvin Bhayani
# 105170206

def pascal(row, column):
    
    if row == 1 :
        return 1
    elif column == 1: 
        return 1
    elif row == column:
        return 1
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)

x = int(input("enter X coordinate:- "))
y =  int(input("Enter Y coordinate:- "))
print(pascal(x,y))