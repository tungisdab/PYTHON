class Gio:
    def __init__(a,x,y,z):
        a.x=x
        a.y=y
        a.z=z
    def __str__(a):
        h=a.z//60
        m=a.z-(a.z//60)*60
        return "{} {} {} gio {} phut".format(a.x, a.y, int(h), int(m))
if __name__=='__main__':
    a=[]
    for _ in range(int(input())):
        x=input()
        y=input()
        p=input()
        q=input()
        p1=int(p[3:5])
        p2=int(q[3:5])
        cc=1
        if p2<p1:
            cc=0
            z2=p2+(60-p1)
        else:
            z2=p2-p1
        if cc==0:
            z1=int(q[0:2])-1-int(p[0:2])
        else:
            z1=int(q[0:2])-int(p[0:2])
        z=z1*60+z2
        # print(z1, z2)
        gio=Gio(x,y,z)
        a.append(gio)
    a=sorted(a, key=lambda m:(m.z), reverse=True)
    for i in a:
        print(i)


