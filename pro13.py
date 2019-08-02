su,ma=map(int,input().split())
lst=list(map(int,input().split()))
l=[]
for i in range(0,ma):
     x,y=map(int,input().split())
     l.append([x,y])
for i in range(ma):
     lwr=l[i][0]
     upr=l[i][1]
     ys=sum(lst[lwr-1:upr])
     print(ys)
