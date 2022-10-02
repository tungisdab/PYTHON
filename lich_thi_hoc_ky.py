class Mon:
    def __init__(a, a0, a1, a2, a3, a4, a5, a6, a7, a8):
        a.a0=a0
        a.a1=a1
        a.a2=a2
        a.a3=a3
        a.a4=a4
        a.a5=a5
        a.a6=a6
        a.a7=a7
        a.a8=a8
    def __str__(a):
        if a.a0>99:
            return "T{} {} {} {}/{}/{} {}:{} {}".format(a.a0, a.a1, a.a2, a.a3, a.a4, a.a5, a.a6, a.a7, a.a8)
        elif a.a0>9:
            return "T0{} {} {} {}/{}/{} {}:{} {}".format(a.a0, a.a1, a.a2, a.a3, a.a4, a.a5, a.a6, a.a7, a.a8)
        else:
            return "T00{} {} {} {}/{}/{} {}:{} {}".format(a.a0, a.a1, a.a2, a.a3, a.a4, a.a5, a.a6, a.a7, a.a8)
if __name__=='__main__':
    arr=[]
    n,m=map(int, input().split())
    maMon=[]
    tenMon=[]
    for _ in range(n):
        maMon.append(input())
        tenMon.append(input())
    for j in range(m):
        ma1, ngay, gio1, nhom=map(str, input().split())
        for i in range(n):
            if ma1==maMon[i]:
                ma=tenMon[i]
                break
        ng,th,na=ngay.split("/")
        gio, phut=gio1.split(":")
        arr.append(Mon(j+1,ma1, ma, ng, th, na, gio, phut, nhom))
    arr.sort(key=lambda m:(m.a5, m.a4, m.a3, m.a6, m.a7, m.a1))
    for i in arr:
        print(i)