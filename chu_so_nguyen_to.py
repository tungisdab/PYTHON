from math import sqrt
def prime(n):
    if n<2:
        return False
    if n<4:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    cnt=0
    s=input()
    l=len(s)
    for i in s:
        if i=='2' or i=='3' or i=='5' or i=='7':
            cnt+=1
    print("YES" if prime(l) and cnt>(l-cnt) else "NO")