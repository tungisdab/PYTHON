from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=[int(i) for i in input().split()]
b=[]
for i in a:
    if prime(i):
        b.append(i)
b.sort()
j=0
for i in a:
    if prime(i):
        print(b[j], end=' ')
        j+=1
    else:
        print(i, end=' ')