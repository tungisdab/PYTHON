def fibo(n):
    f0=0
    f1=1
    fn=1
    if n==1 or n==0:
        return n
    for i in range(2,n):
        f0=f1
        f1=fn
        fn=f0+f1
    return fn
for _ in range(int(input())):
    a,b=input().split()
    a=int(a)
    b=int(b)
    for i in range(a,b+1):
        print(fibo(i),end=' ')
    print()