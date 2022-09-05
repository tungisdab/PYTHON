for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    for i in range(0,n):
        cnt=1
        for j in range(0,i):
            if a[j]<a[i]:
                cnt+=1
        print(cnt, end=' ')
    print()