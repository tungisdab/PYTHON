s=input()
l=len(s)
if l%2==1:
    l-=1
a=[]
for i in range(0,l,2):
    sum=int(s[i])*10+int(s[i+1])
    if sum not in a:
        a.append(sum)
print(*a)