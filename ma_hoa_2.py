p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while 1:
    a=input().split()
    k=int(a[0])
    if k==0:
        break
    s=a[1]
    cc=''
    for i in s:
        cc+=p[(p.find(i)+k)%28]
    ss=''.join(reversed(cc))
    print(ss)