from math import gcd
n,k=input().split()
n=int(n)
k=int(k)
cnt=0
for i in range(10**(k-1),10**k):
    if gcd(n,i)==1:
        cnt+=1
        print(i,end=' ')
        if cnt%10==0:
            print()