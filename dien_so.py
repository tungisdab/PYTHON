for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    cnt=0
    n=len(a)
    for i in range(1,n):
        if a[i]!=a[i-1]:
            cnt=cnt+a[i]-a[i-1]-1
    print(cnt)

    