a=int(input())
li=list(map(int,input().split()[:a]))
t=max(li)
x,y=0,0
for i in range(0,len(li)-1):
    for j in range(i+1,len(li)):
        if(abs(li[i]+li[j])<t):
            x,y=li[i],li[j]
            t=abs(x+y)
print(x,y)