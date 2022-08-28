s=input()
l=len(s)
a=0
b=0
for i in range(l):
    if ord(s[i])<97:
        a+=1
    else:
        b+=1
if a>b:
    print(s.upper())
else:
    print(s.lower())