# Dhruvin Bhayani
# 105170206

import random


list_birthday = []
maximum_days = 365

for i in range(1, maximum_days):
    random_birthday = random.randint(i, maximum_days)

    if random_birthday in list_birthday:
        print('Birthdays that are generated before duplicate: %s' %(len(list_birthday)))
        break
    list_birthday.append(random_birthday)