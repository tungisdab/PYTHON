from ctypes import sizeof
import itertools
for _ in range(int(input())):
    n=int(input())
    a=''
    h=1
    for i in range(1,n+1):
        h*=i
    while n>0:
        a+=str(n)
        n-=1
    nn=itertools.permutations(a)
    print(h)
    for i in nn:
        print(''.join(i), end=' ')
    print()