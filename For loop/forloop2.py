a = int(input())
k=[]
for i in range(2,2*a+1):

    if i<a+2:

        for j in range(1,i):
            k.append(j)

        print(k)
        k=[]

    else:
        for l in range(1,2*a+2-i):
            k.append(l)

        print(k)
        k=[]