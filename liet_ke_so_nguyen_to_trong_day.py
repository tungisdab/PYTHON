from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=[int(i) for i in input().split()]
arr={}
for i in a:
    if i in arr:
        arr[i]+=1
    else:
        arr[i]=1
s=dict.fromkeys(a)
for i in arr:
    if prime(i):
        print(i,arr[i])

