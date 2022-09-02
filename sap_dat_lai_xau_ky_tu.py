for j in range(int(input())):
    a=input()
    b=input()
    cc='YES'
    if len(a) != len(b):
        cc='NO'
    aa=[]
    bb=[]
    for i in a:
        aa.append(i)
    for i in b:
        bb.append(i)
    aa.sort()
    bb.sort()
    if aa!=bb:
        cc='NO'
    j=str(j+1)
    print("Test "+j+': ',end='')
    print(cc)