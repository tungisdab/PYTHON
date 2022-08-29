for _ in range(int(input())):
    n=input()
    cnt=0
    while cnt<=1000:
        cnt+=1
        if int(n)%7==0:
            print(n)
            break
        s=''.join(reversed(n))
        n=int(s)+int(n)
        n=str(n)
    if cnt>1000:
        print(-1)