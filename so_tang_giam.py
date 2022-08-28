for _ in range(int(input())):
    s=input()
    l=len(s)
    ll=0
    rr=0
    cc=1
    if l<3:
        cc=0
    else:
        for i in range(1,l):
            if s[i-1]<s[i] and rr==0:
                ll=1
            elif s[i-1]>s[i] and ll==1:
                rr=1
            else:
                cc=0
    print("YES" if cc==1 and rr==1 else "NO")