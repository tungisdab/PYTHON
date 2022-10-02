class Ts:
    def __init__(a, x, y, z ,w):
        a.x=x
        a.y=y
        a.z=z
        a.w=w
    def __str__(a):
        return "{} {} {} {}".format(a.x, a.y, a.z, a.w)
if __name__=='__main__':
    arr=[]
    maTeam=[]
    tenTeam=[]
    n=int(input())
    for i in range(n):
        maTeam.append(input())
        tenTeam.append(input())
    m=int(input())
    for i in range(m):
        if i>99:
            x='C'+str(i+1)
        elif i>9:
            x='C0'+str(i+1)
        else:
            x='C00'+str(i+1)
        ten=input()
        xx=input()
        p=int(xx[4:])-1
        h1=maTeam[p]
        h2=tenTeam[p]
        arr.append(Ts(x, ten, h1, h2))
    arr.sort(key=lambda m:(m.y))
    for i in arr:
        print(i)    
