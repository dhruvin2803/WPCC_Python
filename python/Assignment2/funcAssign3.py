# Dhruvin Bhayani
# 105170206

def lowestCommonMultiple(a, b):

   if a > b:
       temp = a
   else:
       temp = b

   while(True):
       if((temp % a == 0) and (temp % b == 0)):
           lcm = temp
           break
       temp += 1

   return lcm

# just for testing
# print(lowestCommonMultiple(7,5))