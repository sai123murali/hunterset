a,b=map(int,input().split())
li1=list(map(int,input().split()[:a]))
li2=list(map(int,input().split()[:b]))
for i in li2:
    flag=0
    if(i in li1)and(li1.count(i)==li2.count(i)):
        flag=1
if(flag==1):
    print("YES")
else:
    print("NO")
