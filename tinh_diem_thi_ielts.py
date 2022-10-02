arr=[0, 0, 0, 2.5, 2.5, 3, 3, 3.5, 3.5, 3.5, 4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 5, 5.5, 5.5, 5.5, 6, 6, 6, 6, 6.5, 6.5, 6.5, 7, 7, 7, 7.5, 7.5, 8, 8, 8.5, 8.5, 9, 9]
for _ in range(int(input())):
    a,b,c,d=list(map(float, input().split()))
    a=arr[int(a)]
    b=arr[int(b)]
    z=(float(a)+float(b)+float(c)+float(d))/4
    # print(a,b,c,d)
    # print(z)
    zz=(z*100)%100
    if zz>=75:
        z=int(z)+1
    elif zz>=25 and zz<75:
        z=int(z)+0.5
    elif zz<25:
        z=int(z)
    print('%.1f'%z)
