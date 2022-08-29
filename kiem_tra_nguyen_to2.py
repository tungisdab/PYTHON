def prime(n):
    if n<2:
        return 0
    for i in range(2, n):
        if n%i==0:
            return 0
    return 1

n, m=input().split()
n=int(n)
m=int(m)
a=[]
for i in range(n):
    x=input()
    a.append(x)
for x in a:
    x=x.split()
    for j in x:
        j=int(j)
        if prime(j)==1:
            print(1, sep=' ', end=' ')
        else:
            print(0, sep=' ', end=' ')
    print()


