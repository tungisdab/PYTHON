n=input()
while len(n)>1:
    z=len(n)
    nn=z//2
    a=n[:nn]
    b=n[nn:]
    zz=int(a)+int(b)
    n=str(zz)
    print(n)