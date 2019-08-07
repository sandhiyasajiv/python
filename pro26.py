s=int(input())
p=list(map(int,input().split()))
t=[]
d=1
for i in p:
    if i not in t:
        t.append(i)
        
        
for i in range(len(t)-1):
	if t[i]<t[i+1]:
		d+=1
print(d)
