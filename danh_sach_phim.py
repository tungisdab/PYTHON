class Phim:
    def __init__(a, a1, a2, a3, a4, a5, a6, a7):
        a.a1=a1
        a.a2=a2
        a.a3=a3
        a.a4=a4
        a.a5=a5
        a.a6=a6
        a.a7=a7

    def __str__(a):
        return "{} {} {}/{}/{} {} {}".format(a.a1, a.a2, a.a3, a.a4, a.a5, a.a6, a.a7)
if __name__=='__main__':
    a=[]
    t,n=map(int, input().split())
    TL=[]
    for _ in range(t):
        TL.append(input())
    for j in range(1, n+1):
        tl=input()
        ng,t,na=input().split("/")
        ten=input()
        so=int(input())
        tll=TL[int(tl[2:])-1]
        if j>99:
            P='P'+str(j)
        elif j>9:
            P='P0'+str(j)
        else:
            P='P00'+str(j)
        a.append(Phim(P,tll,ng,t,na,ten,so))
    a.sort(key=lambda m:(m.a5, m.a4, m.a3, m.a6, -m.a7))
    for i in a:
        print(i)
        
