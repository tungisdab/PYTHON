from pickle import BINGET


while True:
    n=int(input())
    if n==0:
        break
    max=0
    min=0
    for i in range(n):
        x=int(input())
        if i==0:
            max=x
            min=x
        else:
            if x>max:
                max=x
            if x<min:
                min=x
    if max==min:
        print("BANG NHAU")
    else:
        print(min, max)