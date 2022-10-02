class SinhVien:
    def __init__(a, x, y, mm1, mm2, mm3):
        a.x=x
        a.y=y
        a.m=mm1+mm2+mm3
        
    def tinh(a):
        a.m=float((int(a.m*10))/10)
    def __str__(a):
        return "{} {} {}".format(a.x, a.y, a.m)
if __name__ == '__main__':
    ten=input()
    dob=input()
    m1=float(input())
    m2=float(input())
    m3=float(input())
    sv=SinhVien(ten, dob, m1, m2, m3)
    sv.tinh()
    print(sv)