for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    arr={}
    for i in a:
        if i in arr:
            arr[i]+=1
        else:
            arr[i]=1
    b=[]
    for i in arr:
        if arr[i]>=(n//2)+1:
            b.append(i)
    if len(b)>0:
        b.sort()
        print(b[0])
    else:
        print("NO")