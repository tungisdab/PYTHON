for _ in range(int(input())):
    s=input()
    l=len(s)
    cc=1
    for i in range(l):
        if s[i]!='0' and s[i]!='1' and s[i]!='2':
            cc=0
            break
    print("YES" if cc==1 else "NO")