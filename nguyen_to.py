from math import gcd

def check(h):
    m=1
    if(h<2):
        m=0
        return m
    for p in range(2, h):
        if h%p==0:
            m=0
            return m
    return m
for _ in range(int(input())):
    n=int(input())
    k=0
    for i in range(n):
        if gcd(i+1, n)==1:
            k+=1
    if check(k)==1:
        print('YES')
    else:
        print('NO')    

