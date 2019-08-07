v=int(input())
l3=list(map(int,input().split()))
l3.sort()
p=0
t=0
for i in range(len(l3)):
    if l3[i]>=p:
        t=t+1
    p=p+l3[i]
print(t)
