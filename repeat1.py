n=int(input())
k=0
lst=input()
lst=lst.split()
lst=list(map(int,lst))
new=[]
for i in range(0,n):
    if((lst.count(lst[i]))>=2):
      if lst[i] not in new:
        new.append(lst[i])
        k=1
if(k==0):
  print("unique")
else:
  for i in range(0,n):
    print(min(new),end=" ")
    new.remove(min(new))
