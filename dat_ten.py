# n,k=list(map(int, input().split()))
n,k=map(int, input().split())
arr=[str(i) for i in input().split()]
az=list(map(str, set(arr)))
a=[0]*1000
def out():
    for i in range(1,k+1):
        print(az[a[i]-1], end=' ')
    print()
def Try(i):
    for j in range(a[i-1]+1,n-k+i+1): 
        a[i]=j
        if i==k:
            out()
        else:
            Try(i+1)
az.sort()
n=len(az)
Try(1)
