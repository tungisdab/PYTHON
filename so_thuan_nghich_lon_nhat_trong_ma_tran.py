from math import sqrt
def check(n):
    n=str(n)
    if len(n)<2:
        return False
    nn=''.join(reversed(n))
    if nn!=n:
        return False
    return True
n,m=input().split()
n=int(n)
m=int(m)
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
max=0
for i in range(n):
    for j in range(m):
        if check(a[i][j]) and a[i][j]>max:
            max=a[i][j]
if max!=0:
    print(max)
    for i in range(n):
        for j in range(m):
            if a[i][j]==max:
                i=str(i)
                j=str(j)
                print('Vi tri ['+i+']['+j+']')
                i=int(i)
                j=int(j)
else:
    print('NOT FOUND')