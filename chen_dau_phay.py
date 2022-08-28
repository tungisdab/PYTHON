s=input()
l=len(s)
if l%3==0:
    for i in range(1,l+1):
        if i!=l and i%3==0:
            print(s[i-1],",",sep="",end="")
        else:
            print(s[i-1],sep="",end="")
elif l%3==2:
    for i in range(1,l+1):
        if i!=l and (i+1)%3==0:
            print(s[i-1],",",sep="",end="")
        else:
            print(s[i-1],sep="",end="")
else:
    for i in range(1,l+1):
        if i!=l and (i+2)%3==0:
            print(s[i-1],",",sep="",end="")
        else:
            print(s[i-1],sep="",end="")