s,r=map(int,input().split())
a=list(map(int,input().split()))
m=list(map(int,input().split()))
t=[]
b=0
for i in range(t):
    x=r[i]/a[i]
    r.append(x)
while r>=0 and len(r)>0:
    mindex=r.index(max(r))
    if r>=a[mindex]:
        b=b+m[mindex]
        r=r-a[mindex]
    a.pop(mindex)
    m.pop(mindex)
    r.pop(mindex)
print(b)
