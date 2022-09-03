for _ in range(int(input())):
    a,b,c=input().split()
    aa=[int(i) for i in input().split()]
    bb=[int(i) for i in input().split()]
    cc=[int(i) for i in input().split()]
    z=[]
    zz=0
    for i in aa:
        if (i in bb) and (i in cc):
            z.append(i)
            zz=1
    if zz==0:
        print('NO')
    else:
        print(*z)