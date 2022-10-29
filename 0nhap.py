import math


class Student(object):

    def __init__(self, id, name, diem):
        self.name = name
        self.diem = diem
        self.id = id
        sum = 0.0
        for i in range(10):
            if i == 0 or i == 1:
                sum = float(sum)+diem[i]*2
            else:
                sum = float(sum)+diem[i]
        sum /= 12
        sum *= 100
        sum = math.floor(sum)
        f = int(sum % 10)
        if f >= 5:
            sum = (sum+10-f)/100
        else:
            sum = (sum-f)/100
        self.tb = sum

    def xeploai(self):
        if self.tb >= 9:
            return "XUAT SAC"
        if self.tb >= 8.0:
            return "GIOI"
        if self.tb >= 7.0:
                return "KHA"
        if self.tb >= 5.0:
            return "TB"
        return "YEU"

        def ma(self):
            id = "HS"
            if self.id < 10:
                id += "0" + str(self.id)
            else:
                id += str(self.id)
        return id

    def __str__(self):
        return self.ma() + " " + self.name + " " + str(self.tb) + " " + self.xeploai()


n = int(input())
a = []
for i in range(n):
    ten = input()
    diem = [float(i) for i in input().split()]
    temp = Student(i+1, ten, diem)
    a.append(temp)
a.sort(key=lambda x: (-x.tb))
for i in a:
    print(i)
