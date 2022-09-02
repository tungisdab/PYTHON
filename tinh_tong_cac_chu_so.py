for _ in range(int(input())):
    s=input()
    a=[]
    sum=0
    for i in s:
        if i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9':
            a.append(i)
        else:
            sum+=int(i)
    a.sort()
    a.append(sum)
    print(*a,sep='')