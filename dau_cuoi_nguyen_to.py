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
    ll=(ord(s[0])-48)*100+(ord(s[1])-48)*10+ord(s[2])-48
    rr=ord(s[l-1])-48+(ord(s[l-2])-48)*10+(ord(s[l-3])-48)*100
    print("YES" if check(ll)==1 and check(rr)==1 else "NO")