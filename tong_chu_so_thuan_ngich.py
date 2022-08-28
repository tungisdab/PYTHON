def check(s):
    s=str(s)
    if len(s)<2:
        return False
    # ss=list(s)
    # ss.reverse()
    ss=''.join(reversed(s))
    return True if ss==s else False
for _ in range(int(input())):
    n=input()
    s=0
    for i in n:
        s+=int(i)
    print("YES" if check(s) else "NO") 