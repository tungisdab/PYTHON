for _ in range(int(input())):
    s=input()
    l=len(s)
    for i in range(l):
        if ord(s[i])-48<10 and ord(s[i])-48>0:
            for j in range(ord(s[i])-48):
                print(s[i-1],end='')
    print()
    