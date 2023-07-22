class Gv:
    def __init__(a,x,y,z,w,t):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
        a.t=t
    def __str__(a):
        if a.x<10:
            return "GV0{} {} {} {:.1f} {}".format(a.x, a.y, a.z, a.w, a.t)
        else:
            return "GV{} {} {} {:.1f} {}".format(a.x, a.y, a.z, a.w, a.t)
if __name__=='__main__':
    a=[]
    for j in range(int(input())):
        s=input()
        ma=input()
        n1=float(input())
        n2=float(input())
        n=n1*2+n2
        if ma[0]=='A':
            ss='TOAN'
        elif ma[0]=='B':
            ss='LY'
        elif ma[0]=='C':
            ss='HOA'
        if ma[1]=='1':
            n+=2
        elif ma[1]=='2':
            n+=1.5
        elif ma[1]=='3':
            n+=1
        elif ma[1]=='4':
            n+=0
        if n>=18:
            nn='TRUNG TUYEN'
        else:
            nn='LOAI'
        # print(j+1, s, ss, n, nn)
        a.append(Gv(j+1, s, ss, n, nn))
    a.sort(key=lambda m:(-m.w))
    for i in a:
        print(i)