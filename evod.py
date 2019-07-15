a=int(input())
li=list(map(int,input().split()[:a]))
for i in range(len(li)):
    if((i%2==0)and(li[i]%2!=0)or(i%2!=0)and(li[i]%2==0)):
        print(li[i],end=" ")