from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=input()
    s=0
    for i in n:
        s+=int(i)
    print("YES" if prime(s) else "NO")