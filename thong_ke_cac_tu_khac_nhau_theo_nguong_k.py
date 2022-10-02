m,n=map(int, input().split())
a={}
for _ in range(m):
    s=input().lower()
    for i in range(len(s)):
        if not s[i].isalnum():
            s=s.replace(s[i], ' ')
    for i in s.split():
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
a=sorted(a.items(), key=lambda m : (-m[1], m[0]))
for i in a:
    if i[1]>=n:
        print(*i)
    else:
        break