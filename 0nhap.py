import math
def prime(n):
    if n<2:
        return False
    if n<4:
        return True
    m=int(math.sqrt(n))+1
    for i in range(2,m):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    print("YES" if prime(n) else "NO")
    print()