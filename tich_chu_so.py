for _ in range(int(input())):
    n=input()
    cc=0
    sum=1
    for i in n:
        if i!='0':
            sum*=int(i)
            cc=1
    print(sum if cc==1 else '0')