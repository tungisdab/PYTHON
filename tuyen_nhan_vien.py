class Nv:
    def __init__(a, x, y, z, w):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
    def __str__(a):
        return "TS0{} {} {:.2f} {}".format(a.x, a.y, a.z, a.w)
if __name__=='__main__':
    a=[]
    for j in range(int(input())):
        s=input()
        n1=float(input())
        n2=float(input())
        if n1>10.0:
            n1/=10
        if n2>10.0:
            n2/=10
        n=(n1+n2)/2
        if n<5:
            ss='TRUOT'
        elif n>=5 and n<8:
            ss='CAN NHAC'
        elif n>=8 and n<=9.5:
            ss='DAT'
        elif n>9.5:
            ss='XUAT SAC'
        a.append(Nv(j+1, s, n, ss))
    a.sort(key=lambda m:(-m.z))
    for i in a:
        print(i)