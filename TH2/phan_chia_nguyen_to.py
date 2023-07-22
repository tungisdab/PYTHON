from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True
q=int(input())
aa=[int(i) for i in input().split()]
a=[]
sum=0
for i in aa:
    if i not in a:
        a.append(i)
        sum+=i
n=len(a)
s1=0
s2=0
cc=-1
for i in range(n):
    s1+=a[i]
    s2=sum-s1
    if prime(s1) and prime(s2):
        cc=i
        break
if cc!=-1:
    print(cc)
else:
    print('NOT FOUND')