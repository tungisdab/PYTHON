for _ in range(int(input())):
    n1,n2,n3=map(int, input().split())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    x,y,z=0,0,0
    arr=[]
    while x<n1 and y<n2 and z<n3:
        if a[x]==b[y]==c[z]:
            arr.append(a[x])
            x+=1
            y+=1
            z+=1
        elif a[x]<b[y]:
            x+=1
        elif b[y]<c[z]:
            y+=1
        else:
            z+=1
    if len(arr)==0:
        print('NO')
    else:
        cc=' '.join(map(str,arr))
        print(cc)