class Sinhvien:
    def __init__(self,name,accepted,submit):
        self.name = name
        self.accepted = accepted
        self.submit = submit
    def __str__(self):
        return "%s %s %s" %(self.name, self.accepted, self.submit)

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        accepted, submit = map(int,input().split())
        arr.append(Sinhvien(name,accepted,submit))
    arr.sort(key=lambda x: (-x.accepted, x.submit, x.name))
    for x in arr:
        print(x)