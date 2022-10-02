import re
a=[]
for _ in range(int(input())):
    x=re.split(r'[A-Za-z]', input())
    for i in x:
        if len(i)>0:
            a.append(int(i))    
a.sort()
for i in a:
    print(i)
