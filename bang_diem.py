import math
class Hs:
    def __init__(a,x,y,z,w):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
    
    def __str__(hs):
        if hs.x<10:
            return "HS0{} {} {} {}".format(hs.x,hs.y,hs.z,hs.w)
        else:
            return "HS{} {} {} {}".format(hs.x,hs.y,hs.z,hs.w)

if __name__=='__main__':
    n=int(input())
    a=[]
    for z in range(1,n+1):
        s=input()
        ss=list(map(float, input().split()))
        sum=0.0
        for i in range(10):
            if i==0 or i==1:
                sum=float(sum)+ss[i]*2
            else:
                sum=float(sum)+ss[i]
        sum/=12
        sum*=100
        sum=math.floor(sum)
        f=int(sum%10)
        if f>=5:
            sum=(sum+10-f)/100
        else:
            sum=(sum-f)/100
        ssum=''
        if sum>=9:
            ssum='XUAT SAC'
        elif sum>=8.0:
            ssum='GIOI'
        elif sum>=7.0:
            ssum='KHA'
        elif sum>=5.0:
            ssum='TB'
        else:
            ssum='YEU'
        hs=Hs(z,s,sum,ssum)
        a.append(hs)
    a=sorted(a,key=lambda x:(x.z), reverse=True)
    for i in a:
        print(i)