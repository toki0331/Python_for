a=[]
b=[0,0,0,0]

for i in range(2,6):

    a=b[0:5-i]

    for j in range(1,i):
        a.append(j)

    print a