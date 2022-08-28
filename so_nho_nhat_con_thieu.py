n=int(input())
a=[int(i) for i in input().split()]
a.sort()
cc=0
if 1<a[0]:
    print(1)
else:
    for i in range(1,n):
        if a[i]-a[i-1]>1:
            cc=a[i-1]+1
            print(cc)
            break
    if cc==0:
        print(a[n-1]+1)