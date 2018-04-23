import copy

k,x=[],[]
a=int(input())
for i in range(2,2*a+1):

    if i<a+2:

        for l in range(1,a+2-i):
            k.append(0)

        for j in range(1,i):
            k.append(j)

        x=copy.deepcopy(k)
        x.pop(-1)
        x.reverse()

        for o in range(0,a-1):
            k.append(x[o])

        print(k)
        x,k=[],[]

    else:

        for l in range(a+1,i):
            k.append(0)

        for l in range(1,2*a+2-i):
            k.append(l)

        x = copy.deepcopy(k)
        x.pop(-1)
        x.reverse()

        for o in range(0,a-1):
            k.append(x[o])
        print(k)
        k,x=[],[]