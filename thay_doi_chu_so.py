for _ in range(int(input())):
    a,b=input().split()
    s11=input()
    s1=""
    s2=""
    a1=s11.split()
    if len(a1)==2:
        s2=a1[1]
        s1=a1[0]
    else :
        s1=s11
        s2=input()
    s=''
    for i in s1:
        if i==b:
            s+=a
        else:
            s+=i
    ss=''
    for i in s2:
        if i==b:
            ss+=a
        else:
            ss+=i
    print(int(s)+int(ss),end=' ')
    s=''
    for i in s1:
        if i==a:
            s+=b
        else:
            s+=i
    ss=''
    for i in s2:
        if i==a:
            ss+=b
        else:
            ss+=i
    print(int(s)+int(ss))