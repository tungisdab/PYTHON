n, m = map(int, input().split())
for i in range(n):
    cc = 0
    x, y = map(int, input().split())
    x = '{:0b}'.format(x).zfill(m)
    y = '{:0b}'.format(y).zfill(m)
    a = set()
    for i in range(m):
        x = x[-1] + x[:-1]
        a.add(x)
    if y in a: 
        cc = 1
    print(1 if cc else 0)
    