# n,k=input().split()
# n=int(n)
# k=int(k)
# a=[]
# def out():
#     for i in range(1,k+1):
#         print(a[i], end=' ')
#     print()
# def tohop(i):
#     for j in range(a[i-1]+1,n-k+i+1):
#         a[i]=j
#         if i==k:
#             out()
#         else:
#             tohop(i+1)
# for i in range(n):
#     a.append(0)
# tohop(1)
# arr=[' ',',']
# a,b,c,d=map(str, input().split())
# print(a,b,c,d)
while True:
    # a=[str(i) for i in input().split()]
    a=input()
    for i in a:
        print(i[0])