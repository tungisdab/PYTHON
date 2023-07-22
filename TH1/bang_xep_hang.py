from telnetlib import XASCII


class SV:
    def __init__(a, x, y, z):
        a.x=x
        a.y=y
        a.z=z
    def __str__(a):
        return "{} {} {}".format(a.x, a.y, a.z)
n=int(input())
a=[]
for i in range(n):
    ten=input()
    ac,sub=map(int, input().split())
    a.append(SV(ten, ac, sub))
a.sort(key=lambda m: (-m.y, m.z, m.x))
for i in a:
    print(i)