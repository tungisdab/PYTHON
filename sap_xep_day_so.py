for _ in range(int(input())):
    n,m=input().split()
    n=int(n)
    m=int(m)
    aa=[int(i) for i in input().split()]
    mm=aa[0]
    dd=0
    for i in range(1,n):
        if mm<aa[i]:
            mm=aa[i]
            dd=i
    aa.insert(dd,m)
    a=[]
    b=[]
    for i in aa:
        if i<0:
            a.append(i)
        else:
            b.append(i)
    print(*a, end=' ')
    print(*b)