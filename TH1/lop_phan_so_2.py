from math import gcd

def ab(m, n):
    return Ps(m, n)

class Ps:
    def __init__(self, m, n):
        self.m=m
        self.n=n
    def add(self, Ps):
        ts=self.m*Ps.n + self.n*Ps.m
        ms=self.n*Ps.n
        return ab(ts, ms)
    def toiGian(self):
        k=gcd(self.m, self.n)
        self.m=self.m/k
        self.n=self.n/k
    def __str__(self):
        return "%s/%s" %(int(self.m), int(self.n))
        
a,b,c,d=list(map(int, input().split()))
x=Ps(a,b)
y=Ps(c,d)
ps=x.add(y)
ps.toiGian()
print(ps)