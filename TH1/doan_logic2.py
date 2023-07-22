def tinh(i):
    if i==1:
        return 0
    return i + tinh(i-1)
n=int(input())
a=[int(i) for i in input().split()]
for i in a:
    print(tinh(i))