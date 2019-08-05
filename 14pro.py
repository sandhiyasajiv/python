v,s=list(map(int,input().split()))
li1=list(map(int,input().split()))
li2=[]
while(s):
	m = list(map(int,input().split()))
	li2.append(m)
	s-=1
for ic in li2:
	val=0
	for jc in range(ic[0]-1,ic[1]):
		val=val^li1[jc]
	print(val)
