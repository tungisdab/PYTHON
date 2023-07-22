thang=[0,31,28,31,30,31,30,31,31,30,31,30,31,0]
def namNhuan(n):
    if n%400==0 or (n%4==0 and n%100!=0):
        return True
    return False
class Ma:
    def __init__(a,x,y,z,p,q):
        a.x=x
        a.y=y
        a.z=z
        a.p=p
        a.q=q
    def __str__(a):
        if a.x<10:
            return "KH0{} {} {} {} {}".format(a.x, a.y, a.z, a.p, a.q)
        else:
            return "KH{} {} {} {} {}".format(a.x, a.y, a.z, a.p, a.q)
if __name__=='__main__':
    a=[]
    n=int(input())
    for j in range(1, n+1):
        x=input()
        y=input()
        ng1,t1,na1=map(int, input().split("/"))
        ng2,t2,na2=map(int, input().split("/"))
        z=int(input())
        soNgay=0
        if na2-na1>1:
            soNgay=(na2-na1-1)*365
            for i in range(na1+1, na2):
                if namNhuan(i):
                    soNgay+=1
        if na2==na1:
            if t1==t2:
                soNgay+=(ng2-ng1+1)
            else:
                if t1==2 and namNhuan(na1):
                    soNgay+=(29-ng1)
                else:
                    soNgay+=(thang[t1]-ng1)
                for i in range(t1+1,t2):
                    if i==2 and namNhuan(na1):
                        soNgay+=29
                    else:
                        soNgay+=thang[i]
                soNgay+=(ng2+1)
        else:
            if t1==2 and namNhuan(na1):
                soNgay+=(29-ng1)
            else:
                soNgay+=(thang[t1]-ng1)
            for i in range(t1+1,13):
                if i==2 and namNhuan(na1):
                    soNgay+=29
                else:
                    soNgay+=thang[i]
            for i in range(1,t2):
                if i==2 and namNhuan(na2):
                    soNgay+=29
                else:
                    soNgay+=thang[i]
            soNgay+=(ng2+1)
        if int(y[0])==1:
            w=soNgay*25+z
        elif int(y[0])==2:
            w=soNgay*34+z
        elif int(y[0])==3:
            w=soNgay*50+z
        elif int(y[0])==4:
            w=soNgay*80+z
        ma=Ma(j,x,y,soNgay,w)
        a.append(ma)
    a=sorted(a, key=lambda m:(m.q), reverse=True)
    for i in a:
        print(i)