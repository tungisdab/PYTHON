import math
class Pss:
    def __init__(a,x,y,z,w,m,n):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
        a.m=m
        a.n=n
    def __str__(a):
        return "{} {} {} {} Km/h".format(a.x, a.y, a.z, a.w)
if __name__=='__main__':
    a=[]
    for i in range(int(input())):
        ten=input()
        dc=input()
        tg1, tg2=map(int, input().split(":"))
        tg=float(tg1-6+float(tg2/60))
        vt=120/tg
        xx=(math.floor(vt*10))%10
        vt=math.floor(vt)
        if xx>=5:
            vt=int(vt)+1
        else:
            vt=int(vt)
        ma=''
        ten1=[str(i) for i in ten.split()]
        dc1=[str(i) for i in dc.split()]
        for i in dc1:
            ma+=i[0]
        for i in ten1:
            ma+=i[0]
        a.append(Pss(ma, ten, dc, vt, tg1, tg2))
    a.sort(key=lambda d:(d.m, d.n))
    for i in a:
        print(i)