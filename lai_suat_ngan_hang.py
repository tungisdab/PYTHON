import math
for _ in range(int(input())):
    arr=[float(i) for i in input().split()]
    k=math.log(arr[2]/arr[0], 1+arr[1]/100)
    k=math.ceil(k)
    print(k)