npit=input()
x1=list(map(int,npit.split()))
y1=x1[1]
ht=input()
flag1=0
sv1=list(map(int,ht.split()))
for i in range(0,len(sv1)-1):
	for j in range(i+1,len(sv1)):
		if sv1[i]+sv1[j]==y1:
			print("yes")
			flag1=2
			break
	if flag1==2:
		break
if flag1!=2:
	print("no")
