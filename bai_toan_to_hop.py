n,k=input().split()
n=int(n)
k=int(k)
a=[]
aa=[]
def out():
    for i in range(1,k+1):
        if i==k:
            print(a[aa[i]-1])
        else:
            print(a[aa[i]-1],end=" ")
def Try(i):
    for j in range(aa[i-1]+1,n-k+i+1):
        aa[i]=j
        if i==k:
            out()
        else:
            Try(i+1)
for i in range(n+1):
    aa.append(0)
b=[int(i) for i in input().split()]
bb=set(b)
a=[*bb]
a.sort()
n=len(a)
if(n>k):
    Try(1)
elif n==k:
    print(*a)



