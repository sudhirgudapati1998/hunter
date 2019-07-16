n=int(input())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
if(max(lst)!=0):
    for i in range(0,n):
        print(max(lst),end="")
        lst.remove(max(lst))
else:
    print("0")
