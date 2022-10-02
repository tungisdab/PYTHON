class Rectangle:
    def __init__(a, dai, rong, mau):
        a.dai=dai
        a.rong=rong
        a.mau=mau

    def perimeter(a):
        return (a.dai+a.rong)*2
    def area(a):
        return a.dai*a.rong
    def color(a):
        return a.mau.capitalize()

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if int(arr[0])<=0 or int(arr[1])<=0:
    print('INVALID')
else:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
        