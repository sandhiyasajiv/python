size8=int(input())
arr2=[]
for j in range(size8):
	vs=input()
	vs=list(map(int,vs.split(" ")))
	nt=len(vs)
	for i in range(nt):
		arr2.append(vs[i])
arr2.sort()
print(*arr3,sep=" ")
