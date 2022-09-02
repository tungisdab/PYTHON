a=[True]*1000005
a[0]=False
a[1]=False
for i in range(2,1000005):
    if a[i]:
        for j in range(2*i,1000005,i):
            a[j]=False
def check(n):
    arr=[]
    for i in range(13,n):
        i=str(i)
        ii=''.join(reversed(i))
        if i!=ii:
            i=int(i)
            ii=int(ii)
            if ii>=n or i>=n:
                continue
            elif (a[i] and a[ii]):
                if i not in arr and ii not in arr:
                    arr.append(i)
                    arr.append(ii)
    print(*arr)
for _ in range(int(input())):
    n=int(input())
    check(n)