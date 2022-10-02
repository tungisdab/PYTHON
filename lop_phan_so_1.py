from math import gcd
class PhanSo:
    def __init__(a,x,y):
        a.x=x
        a.y=y
    def tinh(a):
        z=gcd(a.x, a.y)
        a.x=a.x//z
        a.y=a.y//z
    def __str__(a):
        return "{}/{}".format(a.x, a.y)
def soNguyen(n):
    return int(n)
if __name__ == '__main__':
    a,b=input().split()
    ps=PhanSo(soNguyen(a), soNguyen(b))
    ps.tinh()
    print(ps)    
