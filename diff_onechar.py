x,y=input().split()
a=list(x)
b=list(y)
count=0
for i in range(len(a)):
    if(a[i]==b[i]):
        count=count+1
if(count==(len(a)-1)):
    print("yes")
else:
    print("no")
    
