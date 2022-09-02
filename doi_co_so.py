from re import L


for _ in range(int(input())):
    a,b=input().split()
    arr=[]
    a=int(a)
    b=int(b)
    while a>0:
        if a%b>=10:
            arr.append(chr((a%b)+55))
        else:
            arr.append(a%b)
        a//=b
    n=len(arr)
    while n>0:
        print(arr[n-1],end='')
        n-=1
    print()