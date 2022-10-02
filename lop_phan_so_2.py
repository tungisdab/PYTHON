from math import gcd
def pss(tuSo, mauSo):
    return PhanSo(tuSo, mauSo)

class PhanSo:
    def __init__(a,x,y):
        a.x=x
        a.y=y
    def rutgon(ps):
        zz=gcd(ps.x, ps.y)
        ps.x=ps.x/zz
        ps.y=ps.y/zz

    def solve(ps, PhanSo):
        mauSo=ps.y*PhanSo.y
        tuSo=ps.x*PhanSo.y+ps.y*PhanSo.x
        return pss(tuSo, mauSo)

    def __str__(ps):
        return "{}/{}".format(int(ps.x), int(ps.y))

if __name__ == '__main__':
    a1, b1, a2, b2=map(int, input().split())
    ps1=PhanSo(a1,b1)
    ps2=PhanSo(a2,b2)
    ps=ps1.solve(ps2)
    ps.rutgon()
    print(ps)