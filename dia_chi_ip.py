for _ in range(int(input())):
    s = str(input())
    ok = 1
    for j in s:
        if j.islower():
            ok = 0
            break
    if ok == 1:
        a = s.split('.')
        if len(a) == 4:
            for j in a:
                if int(j) < 0 or int(j) > 255:
                    ok = 0
                    break
        else:
            ok = 0
        if ok == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
