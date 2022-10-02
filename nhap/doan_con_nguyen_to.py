a,b=map(int, input().split())
n=input()

def check(a,b):
    cnt=0
    arr=[True]*2000005
    arr[0]=False
    arr[1]=False
    zz=0
    for i in range(2,2000005):
        if arr[i]==True:
            zz+=1
            if zz>=a and zz<=b:
                s=str(i)
                if n in s:
                    cnt+=1
            if zz>b:
                break
            for j in range(i*2,2000005,i):
                arr[j]=False
    return cnt
print(check(a,b))