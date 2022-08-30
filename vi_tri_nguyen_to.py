from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    s=input()
    l=len(s)
    cc='YES'
    for i in range(l):
        if (prime(i)==False and prime(int(s[i]))==True) or ((prime(int(s[i]))==False and prime(i)==True)):
            cc='NO'
            break
    print(cc)