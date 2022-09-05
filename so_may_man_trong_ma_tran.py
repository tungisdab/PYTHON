n,m=input().split()
n=int(n)
m=int(m)
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
mx=-1
mn=100005
cc=-1
for i in range(n):
    for j in range(m):
        if mx<a[i][j]:
            mx=a[i][j]
        if mn>a[i][j]:
            mn=a[i][j]
cc=(mx-mn)
check=0
for i in range(n):
        for j in range(m):
            if a[i][j]==cc:
                check=1
                break
if check==1:
    print(cc)
    for i in range(n):
        for j in range(m):
            if a[i][j]==cc:
                i=str(i)
                j=str(j)
                print('Vi tri ['+i+']['+j+']')
                i=int(i)
                j=int(j)
else:
    print('NOT FOUND')