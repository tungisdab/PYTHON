for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    b.sort()
    cc='YES'
    for i in range(n):
        if a[i]>b[i]:
            cc='NO'
            break
    print(cc)
