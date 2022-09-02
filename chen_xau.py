s1=input()
s2=input()
n=int(input())
l1=len(s1)
ss=''
for i in range(n-1):
    ss+=s1[i]
ss+=s2
for i in range(n-1,l1):
    ss+=s1[i]
print(ss)
    
    