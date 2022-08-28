from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=input()
    cc=1
    dd=0
    sum=0
    for i in n:
        if dd%2==0:
            if int(i)%2!=0:
                cc=0
                break
        else:
            if int(i)%2!=1:
                cc=0
                break
        dd+=1
        sum+=int(i)
    if prime(sum)==False:
        cc=0
    print("YES" if cc==1 else "NO")