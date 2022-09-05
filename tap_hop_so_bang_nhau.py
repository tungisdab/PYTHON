n,m=input().split()
aa=[int(i) for i in input().split()]
bb=[int(i) for i in input().split()]
a=set(aa)
b=set(bb)
cc='YES'
for i in a:
    if i not in b:
        cc='NO'
        break
print(cc)