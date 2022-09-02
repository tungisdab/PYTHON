arr=[True]*1000005
arr[0]=False
arr[1]=False
for i in range(2,1000005):
    if arr[i]:
        for j in range(2*i,1000005,i):
            arr[j]=False
for _ in range(int(input())):
    n=int(input())
    cnt=0
    for i in range(n-5):
        if (arr[i] and arr[i+2] and arr[i+6]) or (arr[i] and arr[i+4] and arr[i+6]):
            cnt+=1
    print(cnt)