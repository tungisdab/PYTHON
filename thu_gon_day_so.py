from os import remove


n=int(input())
a=[int(i) for i in input().split()]
arr=[]
arr.append(a[0])
i=1
j=0
while i<n:
    if (arr[j]+a[i])%2==0:
        arr.pop()
        l=len(arr)
        if l==0:
            arr.append(a[i+1])
            j=0
            i+=1
        else:
            j=len(arr)-1
    else:
        arr.append(a[i])
        j=len(arr)-1
    i+=1
print(len(arr))

