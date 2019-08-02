
y=int(input())
ys=list(map(int,input().split()))[:y]
sa=sum(ys[0:y:2])
yu=sum(ys[1:y:2])
if sa>yu:
  print(sa)
else:
  print(yu)
