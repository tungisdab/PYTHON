s=[str(i) for i in input()]
a=[]
n=len(s)
i=0
while i<n:
    for _ in range(i):
        a.append(" ")
    if s[i]=='(':
        a.append(s[i]) 
    
        