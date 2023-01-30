import math

file_name = input()
file = open(file_name)
emptylist = []
emptylist2 = []
maxlist = []

for aline in file.readlines():
    points = aline.split()
    if len(points) > 1:
        for apoint in points:
            emptylist.append((float(apoint)))

for i in range(0, len(emptylist), 2):
    emptylist2.append([(emptylist[i]), (emptylist[i+1])])

for i in emptylist2:
    maxlist.append((math.sqrt(((i[0])**2)+((i[1])**2))))
maxlist.sort()

for i in emptylist2:
    if (math.sqrt(((i[0])**2)+((i[1])**2))) == maxlist[0]:
        print(emptylist2.index(i),' (',i[0], ', ', i[1], ') ', float(maxlist[0]), sep='')
        
file.close()