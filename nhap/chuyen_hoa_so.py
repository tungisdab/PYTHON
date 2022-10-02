for _ in range(int(input())):
    a,b=map(int, input().split())
    s=input()
    n=len(s)
    na=0
    for i in s:
        if i=='A':
            na+=1
    nb=n-na
    