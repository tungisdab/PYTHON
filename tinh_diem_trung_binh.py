n=int(input())
a=[float(i) for i in input().split()]
a.sort()
sum=0
dem=0
for i in range(n-1):
    if a[i]!=a[0] and a[i]!=a[n-1]:
        sum=float(sum) + a[i]
        dem+=1
sum=sum/dem
sum='{:.2f}'.format(sum)
print(sum)