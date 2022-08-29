a=set()
t=10 
bb=[]
while t>0: 
    s=input()
    b=s.split() 
    t-=len(b)
    for i in b:
        bb.append(i)
for i in bb:
    a.add(int(i)%42)
print(len(a))
