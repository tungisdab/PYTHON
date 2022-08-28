for _ in range(int(input())):
    a, b= input().split()    
    a=int(a)
    b=int(b)
    arr=[int(i) for i in input().split()]
    print(*arr[b:],*arr[:b])
