n=int(input())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
k=int(input())
s1=0
s2=0
for i in range(n):
    for j in range(i+1,n):
        s1+=a[i][j]
for i in range(n):        
    for j in range(i):
        s2+=a[i][j]
if abs(s1-s2)<=k:
    print('YES')
    print(abs(s1-s2))
else:
    print('NO')
    print(abs(s1-s2))