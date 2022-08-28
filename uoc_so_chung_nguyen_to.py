import math

def Prime(h):
    if h<2:
        return False
    if h<4:
        return True
    if h%2==0 or h%3==0:
        return False
    for p in range(5, h):
        if h%p==0:
            return False
    return True

for _ in range(int(input())):
    a,b=[int(i) for i in input().split()]
    k=math.gcd(a,b)
    s=0
    while k>0:
        s+=k%10
        k=k//10
    print('YES' if Prime(s) else 'NO')