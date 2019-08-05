try:
	num=int(input())
	array=list(map(int,input().split()))
	sa=[]
	for i in array:
		if array.count(i)>1:
			if i not in sa:
				na.append(i)
	print(*sa)
	if len(sa)==0:
		print("unique")
except ValueError:
	print("invalid")
