viji=int(input())
priya=list(map(int,input().split()))
subu=0
for i in range(1,len(priya)-1):
    if priya[i]>priya[i-1] and priya[i]>priya[i+1] or priya[i]<priya[i-1] and priya[i]<priya[i+1]:
        subu+=1
if len(priya)==1:
    print(1)
else:
    print(subu)
