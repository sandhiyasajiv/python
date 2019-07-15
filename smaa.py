ks,k=input().strip().split()
a=int(x)
i=0
while i<len(ks)-1 and k:
 if(RR[i]>RR[i+1]):
  a-=1
  ks=ks[:i]+RR[i+1:]
  if(i!=0):
   i-=1
 else:
  i+=1
mp=ks[:len(ks)-a]
print(mp)
