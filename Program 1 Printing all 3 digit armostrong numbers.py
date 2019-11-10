#Q. To find all the armostrong numbers from 0 to 999.
def armo(x):
    x1=x
    sum=0
    while x>0:
        r=x%10
        x=x//10
        sum=sum+r*r*r
    if sum==x1:
        return True
p=[]
for x in range(100,1000):
    if armo(x):
        p.append(x)
print(p)