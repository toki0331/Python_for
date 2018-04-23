import copy

k,x,y=[],[],[]
a=int(input())
for i in range(2,2*a+1):

    if i<a+2:

        for l in range(1,a+2-i):
            y.append(0)

        for j in range(1,i):
            k.append(j)


        x=copy.deepcopy(k)
        x.pop(-1)
        x.reverse()

        for o in range(0,i-2):
            k.append(x[o])

        y.append(k)

        for p in range(0,a-i):
            y.append(0)

        print(y)
        x,k,y=[],[],[]

    else:

        for l in range(a+1,i):
            y.append(0)

        for l in range(1,2*a+2-i):
            k.append(l)

        x = copy.deepcopy(k)
        x.pop(-1)
        x.reverse()

        for o in range(0,2*a-i):
            k.append(x[o])

        y.append(k)

        for p in range(a+1,i):
            y.append(0)

        print(y)
        x, k, y = [], [], []
