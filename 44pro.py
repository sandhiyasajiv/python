r,s,h,t=map(int,input().split())
b=list(map(int,input().split()))
n=min(b)
for i in range(0,len(b)):
  for j in range(i,len(b)):
    for k in range(j,len(b)):
      val=s*b[i]+h*b[j]+r*b[k]
      if val>n:
        n=val
print(n)
