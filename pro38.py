m,r = map(int,input().split())
l1 = list(map(int,input().split()))
e= 0
for i in l1:
    if(i+r <=5):
        e+=1
v=e//3
print(v)
