s=input()
l=len(s)
sum=0
for i in range(l):
    if s[i]=='4' or s[i]=='7':
        sum+=1
if sum==4 or sum==7:
    print('YES')
else:
    print('NO')