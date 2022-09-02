from itertools import permutations
def Try(s):
    ss=permutations(s)
    for i in ss:
        print(''.join(i))
s=input()
Try(s)