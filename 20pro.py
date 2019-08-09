s,v=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
a=0
for i in range(0,len(l)):
	if v>=l[i]:
	    r=v//l[i]
	    a=a+s
	v=v%l[i]
	if v==0:
		break
print(v)
