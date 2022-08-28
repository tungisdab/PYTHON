from audioop import reverse
from math import gcd
for _ in range(int(input())):
    n=input()
    nn=list(n)
    nn.reverse()
    nn=''.join(nn)
    n=int(n)
    nn=int(nn)
    print("YES" if gcd(n,nn)==1 else "NO")