import re

regex='[\w\s,:]+'
s=""
while True:
    try:
        s+=input()
    except EOFError:
        break
s=re.findall(regex, s)
for i in s:
    tmp=i.lower().split()
    tmp[0]=tmp[0].title()
    print(*tmp)
    # print(' '.join(tmp))