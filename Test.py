#Intro to matrix.
a=[]
b=[]
c=3
d=3
for i in range(c):
    e=int(input(""))
    for j in range(d):
        f=int(input(""))
        b.append(f)
        print("after appending in b",b)
    a.append(e)
    print("After appending a",a)
a.extend(b)
print("After exxtending",a)