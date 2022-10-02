n=int(input())
a=[]
d1=0
d2=0
while n>0:
    n-=1
    s=[str(i) for i in input().split()]
    nn=len(s)
    if nn==7:
        d2+=1
        if d1>0:
            a.append(1)
            d1=0
    else:
        d1+=1
    if d2==4:
        a.append(2)
        d2=0
    if n==0 and d1>0: 
        a.append(1)
print(len(a))
for i in a:
    print(i)