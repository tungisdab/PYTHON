import math
def prime(n):
    if n<2:
        return False
    if n<4:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    if prime(n):
        n=str(n)
        print('1 * '+n+'^1')
    else:
        print('1 * ',end='')
        for i in range(2,n):
            cnt=0
            while n%i==0:
                cnt+=1
                n//=i
            if cnt>0:
                cnt=str(cnt)
                print(i,end='')
                print("^"+cnt,end='' )
                if n>i:
                    print(" * ",end='')
        print()
    
    