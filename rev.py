yu=int(input())-1
li=list(map(int,input().split()))
li=li[::-1]
for i in range(yu):
     print(li[i],end="->")
print(li[yu])
