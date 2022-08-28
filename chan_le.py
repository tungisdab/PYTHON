for _ in range(int(input())):
    a=int(input())
    b=a
    s=b%10
    b=b//10
    h=s
    cc=1
    while b>0:
        k=b%10
        s+=k
        if abs(h-k)==2:
            h=k
        else:
            cc=0
            break
        b=b//10
    if cc==1 and s%10==0:
        print('YES')
    else:
        print('NO')
