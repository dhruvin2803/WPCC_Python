# Dhruvin Bhayani
# 105170206

def subtract(list1, list2):
    list3 = []
    for i in list1:
        if not i in list2:
            list3.append(i)
    return list3

#just for testing 
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [2,6,8]
# print(subtract(l1,l2))
# this shows that nothing is changed in original lists
# print(l1)
# print(l2)