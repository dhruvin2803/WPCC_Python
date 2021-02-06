# Dhruvin Bhayani
# 105170206



def checkCode(productCode):
    splitCode = productCode.split()
    secondHalf = (int(splitCode[1]))
    numberList = []
    if len(splitCode) <= 2:
        for i in range(len(splitCode[0])):
            if splitCode[0][i]>= 'A' and splitCode[0][i]<='Z':
                pass
            elif splitCode[0][i]>='0' and splitCode[0][i]<='9':
                numberList.append(int(splitCode[0][i]))
            else:
                return False
        if len(numberList) > 6:
            return False
        
        if((((numberList[0]*10)+ numberList[1]) * ((numberList[2]*10)+ numberList[3]) * ((numberList[4]*10)+ numberList[5])) == secondHalf):
            return True   
        else:
            return False 
    else:
        return False

   
# Code to test this function
# Pcode = input("Enter the code:- ")
# if checkCode(Pcode) is False:
#     print("False")
# else:
#     print("True")