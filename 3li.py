a=int(input())
li=list(map(int,input().split()[:a]))
for i in range(len(li)):
    for j in range(len(li)):
        for k in range(len(li)):
            if((li[i]+li[j]==li[k])and(i<j<k)):
                print(li[i],li[j],li[k])