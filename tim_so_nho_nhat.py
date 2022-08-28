# for _ in range(int(input())):
#     s=input()
#     l=len(s)
#     t=0
#     cc=1
#     a=[]
#     for i in range(l):
#         if ord(s[i])-48<10 and ord(s[i])-48>=0:
#             if cc==1:
#                 t=0
#             t=t*10+ord(s[i])-48
#             if i==(l-1):
#                 a.append(t)
#             cc=0
#         else:
#             if cc==0:
#                 a.append(t)
#                 cc=1
#     a.sort()
#     print(a[0])
import re

n = int(input())

while n:

    s = input()
    m = re.findall(r'\d+', s)
    m = [int(i) for i in m]
    print(min(m))
    n -= 1