for _ in range(int(input())):
    s=input()
    l=len(s)
    cnt=1
    for i in range(l):
        if i==(l-1) and s[i]==s[i-1]:
            print(cnt,s[i],sep="",end="\n")
        elif i==(l-1) and s[i]!=s[i-1]:
            print(1,s[i],sep="",end="\n")
        elif s[i]!=s[i+1]:
            print(cnt,s[i],sep="",end="")
            cnt=1
        else:
            cnt+=1