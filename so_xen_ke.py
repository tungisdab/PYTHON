for _ in range(int(input())):
    cc='YES'
    n=input()
    l=len(n)
    if l%2==0:
        cc='NO'
    if n[0]==n[1]:
        cc='NO'
    i=0
    while i<l:
        if n[i]!=n[0]:
            cc='NO'
        i+=2
    print(cc)