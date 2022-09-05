s=input()
if len(s)==1:
    print('0')
else:
    res=0
    while len(s)>1:
        n=len(s)
        if s[0]=='-':
            ss=(ord('-')-ord('0'))
        else:
            ss=(ord(s[0])-48)
        for i in range(1,n):
            ss+=(ord(s[i])-48)
        res+=1
        s=str(ss)
    print(res)
# if s[0]=='-':
#     ss=(ord('-')-ord('0'))
# print(ss)
