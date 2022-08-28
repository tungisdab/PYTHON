for _ in range(int(input())):
    s=input()
    l=len(s)
    a=0
    b=0
    a=(ord(s[0])-48)*10+ord(s[1])-48
    b=(ord(s[l-2])-48)*10+ord(s[l-1])-48
    if a==b:
        print('YES')
    else:
        print('NO')