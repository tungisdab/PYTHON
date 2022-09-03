m,n=input().split()
m=int(m)
n=int(n)
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a=set(a)
b=set(b)
abz=[]
ab=[]
ba=[]
for i in a:
    if i in b:
        abz.append(i)
    else:
        ab.append(i)
for i in b:
    if i not in a:
        ba.append(i)
abz.sort()
ab.sort()
ba.sort()
print(*abz)
print(*ab)
print(*ba)

