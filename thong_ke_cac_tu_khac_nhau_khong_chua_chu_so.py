a={}
for _ in range(int(input())):
    s=input().lower()
    for i in range(len(s)):
        if not s[i].isalpha():
            s=s.replace(s[i], ' ')
    for i in s.split():
        if i in a:
            a[i]+=1
        else:
            a[i]=1
a=sorted(a.items(), key=lambda m : (-m[1], m[0]))
for i in a:
    print(*i)