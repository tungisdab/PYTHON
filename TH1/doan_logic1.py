n=int(input())
a=[int(i) for i in input().split()]
for i in a:
    print(2**(i-1)+1)