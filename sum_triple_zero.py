# a=[]
# def check(l,r,value):
#     while(l<=r):
#         m=(l+r)//2
#         if a[m]==value:
#             return True
#         elif a[m]<value:
#             l=m+1
#         else:
#             r=m-1
#     return False
# for _ in range(int(input())):
#     n=int(input())
#     a=[int(i) for i in input().split()]
#     a.sort()
#     cnt=0
#     for i in range(n-2):
#         for j in range(i+1,n-1):
#            if check(j+1,n-1,0-a[i]-a[j]):
#             cnt+=1
#             break
#     print(cnt)
for _ in range(int(input())):
    n=int(input())
    cnt=0
    a=sorted([int(i) for i in input().split()])
    for i in range(n-2):
        l=i+1
        r=n-1
        x=a[i]
        while l<r:
            if x+a[l]+a[r]==0:
                cnt+=1
                l+=1
            elif x+a[l]+a[r]<0:
                l+=1
            else:
                r-=1
    print(cnt)