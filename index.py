n=int(input())
lst=input()
new=[]
k=0
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
    if(lst[i]==i):
        k=1
        new.append(i)
if(k==0):
    print("-1")
else:
    for i in range(0,n):
        print(min(new),end=" ")
        new.remove(min(new))
        
