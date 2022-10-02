import math
class Sv:
    def __init__(a, x, y, z, w):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
    def __str__(a):
        if a.x<10:
            return "SV0{} {} {:.2f} {}".format(a.x, a.y, a.z, a.w)
        else:
            return "SV{} {} {:.2f} {}".format(a.x, a.y, a.z, a.w)
if __name__=='__main__':
    arr=[]
    stt=[]
    tz=[]
    diem=[]
    tt=[]
    ttt=[]
    for j in range(int(input())):
        vv=input()
        ten=''
        for i in vv.split():
            ten+=i.capitalize()
            ten+=' '
        ten=ten.strip()
        stt.append(j+1)
        tz.append(ten)
        d=0
        d1=int(input())
        d2=int(input())
        d3=int(input())
        d=(d1*3 + d2*3 + d3*2)/8
        d=d*1000
        q=d%10
        d=math.floor(d/10)
        if q>=5:
            d+=1
        d=d/100
        diem.append(d)
        tt.append(d)
    tt.sort(reverse=True)
    ttt.append(1)
    max=ttt[0]
    dd=tt[0]
    for i in range(1,len(tt)):
        if tt[i]!= dd:
            max=i+1
            dd=tt[i]
            ttt.append(max)
        else:
            ttt.append(max)
    for i in range(len(tz)):
        for j in range(len(ttt)):
            if diem[i]==tt[j]:
                xx=ttt[j]
                break
        arr.append(Sv(stt[i], tz[i], diem[i], xx))
    arr.sort(key=lambda m:(-m.z, m.x))
    for i in arr:
        print(i)