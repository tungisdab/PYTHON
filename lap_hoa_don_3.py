class Hang:
    def __init__(a, x, y, z, m, n, p):
        a.x=x
        a.y=y
        a.z=z
        a.m=m
        a.n=n
        a.p=p
    def __str__(a):
        return "{} {} {} {} {} {}".format(a.x, a.y, a.z, a.m, a.n, a.p)
        
if __name__ =="__main__":
    a=[]
    for i in range(int(input())):
        ma=input()
        ten=input()
        sl=int(input())
        gia=int(input())
        giam=int(input())
        a.append(Hang(ma, ten, sl, gia, giam, gia*sl-giam))
    a.sort(key=lambda m:(-m.p))
    for i in a:
        print(i)