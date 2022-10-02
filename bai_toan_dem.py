n=int(input())
a=[]
while len(a)<n:
    a.extend(list(map(int, input().strip().split())))
cc=0
a.sort()
for i in range(1,a[n-1]):
    if i not in a:
        print(i)
        cc=1
if cc==0:
    print('Excellent!')