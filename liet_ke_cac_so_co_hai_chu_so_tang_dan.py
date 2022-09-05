s=input()
l=len(s)
if l%2==1:
    l-=1
a=set()
aa=[]
for i in range(0,l,2):
    sum=int(s[i])*10 + int(s[i+1])
    a.add(sum)
for i in a:
    aa.append(i)
aa.sort()
print(*aa)