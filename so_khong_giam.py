for _ in range(int(input())):
    s=input()
    l=len(s)-1
    cc=1
    for i in range(l):
        if s[i]>s[i+1]:
            cc=0
            break
    if cc:
        print('YES')
    else:
        print('NO')
