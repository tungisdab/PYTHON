s=input()
l=len(s)
if l%2==1:
    l-=1
f={}
i=0
while i<l:
    a=int(s[i])*10 + int(s[i+1])
    if a in f:
        f[a]+=1
    else:
        f[a]=1
    i+=2
i=0
while i<l:
    a=int(s[i])*10 + int(s[i+1])
    if f[a]>0:
        print(a, f[a])
        f[a]=0
    i+=2