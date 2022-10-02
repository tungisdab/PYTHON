# from distutils.spawn import spawn


n=int(input())
a=list(map(int, input().split()))
a.sort()
m1=max(a[0]*a[1], a[n-2]*a[n-1])
m2=max(a[0]*a[1]*a[n-1], a[n-3]*a[n-2]*a[n-1])
print(max(m1,m2))