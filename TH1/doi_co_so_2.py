for _ in range(int(input())):
    a=int(input())
    x=input()
    x=int(x,2)
    if a==2:
        print(bin(x)[2:])
    if a==4:
        arr=[]
        while x>0:
            arr.append(x%a)
            x//=a
        arr.reverse()
        print(*arr, sep='')
    if a==8:
        print(oct(x)[2:])
    if a==16:
        x=format(x,'X')
        print(x)