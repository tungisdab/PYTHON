class Hs:
    def __init__(a, x, y, z, w):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
    def __str__(a):
        if a.x<10:
            return "TS0{} {} {} {}".format(a.x, a.y, a.z, a.w)
        else:
            return "TS{} {} {} {}".format(a.x, a.y, a.z, a.w)
if __name__=='__main__':
    a=[]
    for j in range(int(input())):
        s=input()
        ten=''
        for i in s.split():
            ten+=i.capitalize()
            ten+=' '
        ten=ten.strip()
        d=float(input())
        dt=input()
        if dt!='Kinh':
            d+=1.5
        v=int(input())
        if v==1:
            d+=1.5
        if v==2:
            d+=1
        if d<20.5:
            vv='Truot'
        else:
            vv='Do'
        a.append(Hs(j+1, ten, d, vv))
    a.sort(key=lambda m :(-m.z, m.x))
    for i in a:
        print(i)