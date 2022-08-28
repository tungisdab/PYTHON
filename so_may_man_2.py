for _ in range(int(input())):
    s=input()
    l=len(s)
    cc=0
    for i in range(l):
        if s[i]!='4' and s[i]!='7':
            cc+=1
            break
    if cc==0:
        print('YES')
    else:
        print('NO')