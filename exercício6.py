import random
randomlist = []
d = 500000
for i in range(d):
    randomlist.append(random.randint(0,d))

randomlist.sort() 
print(randomlist)