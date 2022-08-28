for _ in range(int(input())):
    s=input()
    l=len(s)
    s1=0
    s2=1
    cc=0
    for i in range(l):
        if i%2==0:
            s1+=int(s[i])
        else:
            if s[i]!='0':
                cc=1
                s2*=int(s[i])
    print(s1, end=' ')
    print("0" if cc==0 else s2)