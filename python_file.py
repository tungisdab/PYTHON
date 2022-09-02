s=input()
s=s.lower()
x=s[len(s)-3:]
if x=='.py' and len(s)>2:
    print('yes')
else:
    print('no')