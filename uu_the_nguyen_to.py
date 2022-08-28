def check(h):
    m=1
    if(h<2):
        m=0
        return m
    for p in range(2, h):
        if h%p==0:
            m=0
            return m
    return m
for _ in range(int(input())):
    s=input()
    l=len(s)
    cc=1
    ll=0
    rr=0
    if check(l)==0:
        cc=0
    for i in range(l):
        if s[i]=='2' or s[i]=='3' or s[i]=='5' or s[i]=='7':
            ll+=1
        else:
            rr+=1
    print("YES" if cc==1 and ll>rr else "NO")