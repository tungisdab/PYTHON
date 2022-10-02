import math
class Mua:
    def __init__(a,x,y,z):
        a.x=x
        a.y=y
        a.z=z
    def __str__(a):
        # a.z=math.floor(a.z*1000)
        # q=a.z%10
        # if q>=5:
        #     a.z=(math.floor((a.z+10)/10))/100
        # else:
        #     a.z=(math.floor(a.z/10))/100
        if a.x<10:
            return "T0{} {} {:.2f}".format(a.x, a.y, a.z)
        else:
            return "T{} {} {:.2f}".format(a.x, a.y, a.z)
if __name__=='__main__':
    a=[]
    b=[]
    c=[]
    for _ in range(int(input())):
        s=input()
        t11, t12=map(int, input().split(":"))
        t21, t22=map(int, input().split(":"))
        tt=int(input())
        if t12>t22:
            t=t21-t11-1+(60+t22-t12)/60
        else:
            t=t21-t11+(t22-t12)/60
        if s not in a:
            a.append(s)
            b.append(tt)
            c.append(t)
        else:
            for i in range(len(a)):
                if s==a[i]:
                    b[i]+=tt
                    c[i]+=t
    for i in range(len(a)):
        q=Mua(i+1,a[i],b[i]/c[i])
        print(q)
        