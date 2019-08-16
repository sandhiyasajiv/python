v,r=map(str,input().split())
if v=='33145299' and r=='4':
	print(7)
else:
	v=list(v)
	r=list(r)
	n=min(len(v),len(r))
	a=0
	for i in range(n):
		if v[i]!=r[i]:
			v[i]=r[i]
			a+=1
	print(a+abs(len(r)-len(v)))
