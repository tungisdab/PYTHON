for _ in range(int(input())):
    a,b=input().split()
    a=int(a)
    b=int(b)
    arr=[]
    while a>0:
        if a%b>=10:
            arr.append(chr((a%b)+55))
        else:
            arr.append(str(a%b))
        a//=b
    arr=''.join(reversed(arr))
    print(*arr,sep='') 