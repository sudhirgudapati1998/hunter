n=int(input())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
    print(max(lst),end="")
    lst.remove(max(lst))
