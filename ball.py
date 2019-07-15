a,b=input().split()
r1=abs(len(a)-len(b))
for k in range(len(b)):
  if(len(a)==1 and a[k] in b):
    break
  if(b[k]!=a[k]):
    r1=r1+1
print(r1)
