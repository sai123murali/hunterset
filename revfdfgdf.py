st=str(input())
a=len(st)
ne=[]
if(a%2!=0):
    st=st[:a//2]+st[(a//2)+1:]
a=len(st)
for i in range(a//2):
    ne.append(st[i])
ne=ne[::-1]
for j in range(len(ne)):
    if(st[j+(a//2)]!=ne[j]):
        print("NO")
        exit()
print("YES")
