a=list(input())
b=list(a)
count=0
b.reverse()
for i in range(len(a)):
    if(a[i]==b[i]):
        count=count+1
if(count==(len(a))):
    print("yes")
else:
    print("no")
