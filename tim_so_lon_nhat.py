import re
for _ in range(int(input())):
    s=input()
    kk=re.findall(r'\d+',s)
    kk=[int(i) for i in kk]
    print(max(kk))