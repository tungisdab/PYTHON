s=input()
cc='YES'
for i in s:
    if i!='6' and i!='8':
        cc='NO'
        break
a = [int(i) for i in s]
for i in range(len(a)):
    if a[0] == 8:
        cc='NO'
    if a[i] == 8 and a[i-1] != 6 and a[i-1] != 8:
        cc='NO'
    if i > 1 and a[i] == 8 and a[i-1] == 8 and a[i-2] != 6:
        cc='NO'
print(cc)