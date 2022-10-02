for _ in range(int(input())):
    n=int(input())
    a=[]
    f={}
    for i in range(n):
        x=int(input())
        if x not in f:
            a.append(x)
            f[x]=1
        else:
            f[x]+=1
    cc=1000000
    max=0
    for i in a:
        if f[i]>max:
            max=f[i]
    for i in a:
        if f[i]==max:
            cc=min(cc, i)
    print(cc)