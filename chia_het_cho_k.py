a, b, c = [int(i) for i in input().split()]
res=-1
c=c//b+1
for i in range(c):
    x=i*b-a
    if x>0:
        res=1
        print(x, end=' ')
if res==-1:
    print(-1)

