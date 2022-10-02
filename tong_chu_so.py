s=input()
res=0
if len(s)==1:
    print('0')
else:
    while len(s)>1:
        n=len(s)
        ss=0
        for i in range(n):
            ss+=(ord(s[i])-ord('0'))
        res+=1
        s=str(ss)
print(res)

