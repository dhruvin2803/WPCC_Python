# Dhruvin Bhayani
# 105170206

import random

names = []

while True:
    inp = input("Enter name of the person(x to exit): ")
    if inp == 'x':
        break
    names.append(inp)

random.shuffle(names)
for i in range(len(names)):
    print(names[i],"gifts",names[(i+1)%(len(names))])
