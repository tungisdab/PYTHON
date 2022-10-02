n=int(input())
zz=0
a=[]
b=[]
cnt=0
while n>0:
    n-=1
    s=input()
    if zz==0:
        a.append(str(s))
        zz=1
    elif zz==1:
        c=[str(i) for i in s.split()]
        if len(c)>0:
            cnt+=1
        if len(c)==0 or n==0:
            b.append(cnt)
            cnt=0
            zz=0
nn=len(a)
for i in range(nn):
    print(a[i],b[i], sep=": ")