class Aa:
    def __init__(a,x,y,z):
        a.x=x
        a.y=y
        a.z=z
    def __str__(a):
        if a.x<10:
            return "KH0{} {} {}".format(a.x, a.y, round(a.z))
        else:
            return "KH{} {} {}".format(a.x, a.y, round(a.z))
if __name__=='__main__':
    a=[]
    n=int(input())
    for j in range(1,n+1):
        x=input()
        y=int(input())
        z=int(input())
        y=z-y
        if y<=50:
            z=0.02
        elif y<=100:
            z=0.03
        else:
            z=0.05
        if y<=50:
            tong=y*100
            y-=50
        else:
            tong=50*100
            y-=50
        if y>0 and y<=50:
            tong=tong+y*150
            y-=50
        elif y>0 and y>50:
            tong=tong+50*150
            y-=50
        if y>0:
            tong=tong+y*200
            y-=50
        aa=Aa(j,x,tong*z+tong)
        a.append(aa)
    a=sorted(a, key=lambda m:(m.z), reverse=True)
    for i in a:
        print(i)