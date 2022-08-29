for _ in range(int(input())):
    s=input()
    ss="".join(reversed(s))
    l=len(s)
    cc=1
    for i in range(1,l):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(ss[i])-ord(ss[i-1])):
            cc=0
    print("YES" if cc==1 else "NO")