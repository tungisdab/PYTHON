n=int(input())
a=[]
while len(a)<n:
    a.extend(list(map(int, input().strip().split())))
c=[]
l=[]
for i in a:
    if i%2==0:
        c.append(i)
    else:
        l.append(i)
c.sort()
l.sort(reverse=True)
i=0
j=0
for k in a:
    if k%2==0:
        print(c[i], end=' ')
        i+=1
    else:
        print(l[j], end=' ')
        j+=1