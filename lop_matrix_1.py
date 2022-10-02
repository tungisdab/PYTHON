for _ in range(int(input())):
    n, m=map(int, input().split())
    a=[]
    b=[]
    c=[]
    for i in range(n):
        a.append([int(j) for j in input().split()])
    for i in range(m):
        b.append([0]*n)
    for i in range(m):
        for j in range(n):
            b[i][j]=a[j][i]
    for i in range(n):
        c.append([0]*n)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                c[i][j]+=(a[i][k]*b[k][j])
    for i in range(n):
        for j in range(n):
            print(c[i][j], end=' ')
        print()