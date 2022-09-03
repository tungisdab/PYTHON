n=int(input())
a=[]
for i in range(n):
    a.append([str(i) for i in input()])
cnt=0
for i in range(n):
    cc=0
    for j in range(n):
        if (str(a[i][j])=='C'):
            cc+=1
    cnt+=((cc*(cc-1))//2)
    cc=0
    for j in range(n):
        if (str(a[j][i])=='C'):
            cc+=1
    cnt+=((cc*(cc-1))//2)
print(cnt)