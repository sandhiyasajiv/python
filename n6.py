s=int(input())
a=list(map(int,input().split()))
r=0
for i in range(s):
  for j in range(i,s):
      for k in range(j,s):
          if(a[i]<a[j]<a[k]):
            r+=1
print(r)
