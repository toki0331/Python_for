a = int(input())
k=[]
for i in range(1,2*a):

    if i<a+1:

        k.append(i)
        print(k)

    else:

        k.pop(-1)
        print(k)
