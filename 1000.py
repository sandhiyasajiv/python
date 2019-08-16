m=int(input())
l=list(map(int,input().split()))
a=0
for i in range(0,m):
    for i in range(0,i):
        if l[i]<l[j]:
            a=a+l[i]
print(a)        
