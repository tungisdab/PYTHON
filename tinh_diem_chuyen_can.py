class Sv:
    def __init__(a,x,y,z,w):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
    def __str__(a):
        if a.w==0:
            return "{} {} {} {} KDDK".format(a.x, a.y, a.z, a.w)
        else:
            return "{} {} {} {}".format(a.x, a.y, a.z, a.w)
if __name__=='__main__':
    n=int(input())
    a=[]
    b=[]
    c=[]
    d=[int(0) for i in range(n)]
    for _ in range(n):
        a.append(input())
        b.append(input())
        c.append(input())
    for i in range(n):
        ma, diem=map(str, input().split())
        for i in range(n):
            dd=10
            if ma==a[i]:
                for j in range(len(diem)):
                    if diem[j]=='v':
                        dd-=2
                    elif diem[j]=='m':
                        dd-=1
                if dd>=0:
                    d[i]=dd
                break
    for i in range(n):
        print(Sv(a[i],b[i],c[i],d[i]))    

