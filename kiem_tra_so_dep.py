for _ in range(int(input())):
    s=input()
    n=len(s)
    cc='YES'
    i=0
    while i<n:
        if s[i]!=s[0]:
            cc='NO'
        i+=2
    i=1
    while i<n:
        if s[i]!=s[1]:
            cc='NO'
        i+=2
    print(cc)