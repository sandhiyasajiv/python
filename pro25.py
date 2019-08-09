sandy=input()
vsan=list(map(int,input().split()))
max=0
k=0
while(k<len(vsan)-1):
    count=0
    while(k<len(vsan)-1 and vsan[k]<vsan[k+1]):
        count+=1
        k+=1
    if(count>max):
        max=count
    k+=1
print(max+1)
