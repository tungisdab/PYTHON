s=input()
k=int(input())
l=len(s)
if l%2==1:
    l-=1
a=[]
f={}
for i in range(0,l,2):
    sum=int(s[i])*10+int(s[i+1])
    if sum not in a:
        a.append(sum)
        f[sum]=1
    else:
        f[sum]+=1
a.sort()
cc=0
for i in a:
    if f[i]>=k:
        print(i, f[i])
        cc=1
if cc==0:
    print("NOT FOUND")
