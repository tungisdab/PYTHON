n,m=list(map(int, input().split()))
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
if n==m:
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()
elif n>m:
    z=0
    for i in range(n):
        if i%2==0 and z<(n-m):
            z+=1
        else:
            for j in range(m):
                print(a[i][j], end=' ')
            print()
else:
    for i in range(n):
        z=0
        for j in range(m):
            if j%2==1 and z<(m-n):
                z+=1
            else:
                print(a[i][j], end=' ')
        print()
