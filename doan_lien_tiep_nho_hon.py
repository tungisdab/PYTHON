# for _ in range(int(input())):
#     n=int(input())
#     a=[int(i) for i in input().split()]
#     aa=[]
#     n=n-1
#     cnt=1
#     aa.append(1)
#     while n>=0:
#         if a[n-1]<=a[n]:
#             cnt+=1
#             aa.pop()
#             aa.append(cnt)
#         else:
#             cnt=1
#             a.append(cnt)
#         n-=1
#     print(*aa)    
# 
# 
#         
# t = int (input ())
# while t :
#     t-=1 
#     n = int (input())
#     a = [ int(i) for i in input().split()]
#     b= []
#     c= [0]* (len(a))
#     for i in range (0, len (a)):
#         cnt = i
#         while (len(b) != 0 and a[i] >= a[ b[len(b)-1] ] ):
#             b.pop()
#         if (len(b)==0) : c[i] = -1 ;
#         else : c[i] = b[len(b)-1 ]
#         b.append(i)
#     for  i in range (0, len (a)):
#         print (i-c[i], end=" ")
#     print ("")
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[]
    c=[0]*n
    for i in range(n):
        cnt=i
        while(len(b)!=0 and a[i]>=a[b[len(b)-1]]):
            b.pop()
        if len(b)==0:
            c[i]=-1
        else:
            c[i]=b[len(b)-1]
        b.append(i)
    for i in range(n):
        print(i-c[i], end=' ')
    print()