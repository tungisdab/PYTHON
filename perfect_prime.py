from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check(n):
    sum=0
    l=len(n)
    for i in range(l):
        if (n[i]!='2' and n[i]!='3' and n[i]!='5' and n[i]!='7'):
            return False
        else:
            sum+=int(n[i])
    return(True if prime(sum) else False)
for _ in range(int(input())):
    n=input()
    nn=''.join(reversed(n))
    cc='Yes'
    if check(n)==False:
        cc='No'
    n=int(n)
    nn=int(n)
    if prime(n)==False or prime(nn)==False:
        cc='No'
    print(cc)
