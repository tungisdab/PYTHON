a=[str(i) for i in input().split()]
b=[str(i) for i in input().split()]
aa=set()
bb=set()
for i in a:
    aa.add(i.lower())
for i in b:
    aa.add(i.lower())
for i in a:
    x=i.lower()
    for j in b:
        y=j.lower()
        if x==y:
            bb.add(x)
az=[]
bz=[]
for i in aa:
    az.append(i)
for i in bb:
    bz.append(i)
az.sort()
bz.sort()
print(*az)
print(*bz)

