arr=[]
for _ in range(int(input())):
    x=input()
    y=input()
    z=input()
    arr.append([x, y, z])
arr=sorted(arr, key = lambda m: m[0])
a=[]
for i in arr:
    if i[2] == "Turned in late" and (i[1].isdigit() or i[1][:2] != "No") :
        a.append(i[0].replace(" - ", "-").split("-")[0])
print(len(a))
for i in a:
    print(i)