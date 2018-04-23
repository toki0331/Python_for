a=[]


def fin(n):
    results=[]
    a,b =0,1
    while a<n:
        results.append(a)
        a,b=b,a+b
    return results


a=fin(100)
print(a)
