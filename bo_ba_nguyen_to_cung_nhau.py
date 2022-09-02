from math import gcd
a,b=input().split()
a=int(a)
b=int(b)+1
for i in range(a,b-2):
    for j in range(i+1,b-1):
        for k in range(j+1,b):
            if (gcd(i,j)==1 and gcd(j,k)==1 and gcd(i,k)==1):
                print('(',end='')
                print(i,j,k, sep=', ',end=')')
                print()