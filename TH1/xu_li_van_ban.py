import re

st=""
regex='[\w\s,:]+'
while True:
    try:
        st+=input()
    except EOFError:
        break
st=re.findall(regex, st)
for i in st:
    tmp= i.lower().split()
    tmp[0]=tmp[0].title()
    # ss=' '.join(tmp)
    # print(*tmp)
    print(' '.join(tmp))