def check(n):
    res=0
    n=str(n)
    for i in n:
        res+=int(i)
    return res
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    for i in range(n-1):
        for j in range(i+1,n):
            if((check(a[i])>check(a[j])) or (check(a[i])==check(a[j]) and a[i]>a[j])):
                a[i], a[j]=a[j],a[i]
    print(*a)