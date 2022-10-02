def pss(a,b):
    return SoPhuc(a,b)

class SoPhuc:
    def __init__(x,a,b):
        x.a=a
        x.b=b

    def solve1(x, SoPhuc):
        m=x.a+SoPhuc.a
        n=x.b+SoPhuc.b
        return pss(m,n)
    
    def solve2(x, SoPhuc):
        m=x.a*SoPhuc.a-x.b*SoPhuc.b
        n=x.a*SoPhuc.b+x.b*SoPhuc.a
        return pss(m,n)

    def __str__(x):
        if (x.b>=0):
            return "{} + {}".format(int(x.a), int(x.b))
        else:
            return "{} - {}".format(int(x.a), abs(int(x.b)))
if __name__=='__main__':
    for _ in range(int(input())):
        a,b,c,d=map(int, input().split())
        a1=SoPhuc(a,b)
        a2=SoPhuc(c,d)
        a3=a1.solve1(a2)
        a4=a1.solve1(a2)
        print(a3.solve2(a1),end='i, ')
        print(a4.solve2(a4),end='i')
        print()