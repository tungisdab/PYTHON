class Mon:
    def __init__(a, x, y, z):
        a.x=x
        a.y=y
        a.z=z
    def __str__(a):
        return "{} {} {}".format(a.x, a.y, a.z)
if __name__=='__main__':
    a=[]
    for _ in range(int(input())):
        x=input()
        y=input()
        z=input()
        mon=Mon(x,y,z)
        a.append(mon)
    a=sorted(a, key=lambda m:(m.x))
    for i in a:
        print(i)        