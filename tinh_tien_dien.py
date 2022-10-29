
if __name__=="__main__":
    a=[]
    nn=int(input())
    for i in range(1,nn+1):
        ss=list(map(str, input().split()))
        name=""
        for i in ss:
            name+=i.capitalize()
            name+=" "
        name.strip()
        print(name)
        id, sd1, sd2=map(str, input().split())
        sd=int(sd2)-int(sd1)
        vuot=0
        if id=='A':
            if sd>=100:
                vuot=sd-100

        elif id=='B':
            if sd>=500:
                vuot=sd-500

        elif id=='C':
            if sd>=200:
                vuot=sd-200
