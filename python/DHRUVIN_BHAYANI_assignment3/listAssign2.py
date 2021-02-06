# Dhruvin Bhayani
# 105170206


month_list = [1,2,3,4,5,6,7,8,9,10,11,12]

day_list = [31,28,31,30,31,30,31,31,30,31,30,31]

print("list of months:- ", month_list)
print("list of days in month:- ", day_list)

#input from user
month_num = int(input("Enter Month: "))
day_num = int(input("Enter Day: "))

#calculation into days
numberOfDay = sum(day_list[0:month_num -1])
numberOfDay = numberOfDay + day_num

print("Calculated day of the year: ", numberOfDay)