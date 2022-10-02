n,m=list(map(int, input().split()))
a=[int(i) for i in input().split()]
f={}
aa=[]
for i in a:
    if i not in f:
        f[i]=1
        aa.append(i)
    else:
        f[i]+=1
a=set(a)
m=0
cnt=0
res=0
for i in a:
    if m<f[i]:
        m=f[i]
        cnt+=1
if cnt==1:
    print('NONE')
else:
    for i in a:
        if res<f[i] and f[i]<m:
            res=f[i]
    for i in aa:
        if f[i]==res:
            print(i)
            break
