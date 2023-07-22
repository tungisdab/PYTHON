n=int(input())
a={}
cc='Yes'
for _ in range(n-1):
    m,n = map(int, input().split())
    if m in a:
        a[m]+=1
    else:
        a[m]=1
    if n in a:
        a[n]+=1
    else:
        a[n]=1
for i in range(1, n+1):
    if (i not in a) or (a[i]!=1 and a[i]!=n-1):
        cc='No'
        break
print(cc)

