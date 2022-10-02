for _ in range(int(input())):
    s=input()
    a=1
    b=0
    arr1=[]
    arr2=[]
    for i in s:
        if i=='(':
            arr1.append(a)
            arr2.append(a)
            a+=1
        if i==')':
            arr1.append(arr2[len(arr2)-1])
            arr2.pop()
    for i in arr1:
        print(i, end=' ')
    print()