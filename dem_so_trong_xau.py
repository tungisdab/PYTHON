for _ in range(int(input())):
    s=input()
    x=input()
    ls=len(s)
    lx=len(x)
    dem=0
    i=0
    while i<=(ls-lx):
        s1=str(s[i:(i+lx)])
        if s1==x:
            dem+=1
            i=i+lx
        else:
            i=i+1
    print(dem)
