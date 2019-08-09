m=int(input())
li=list(map(int,input().split()))
a=0
for i in range(1,len(li)):
    if (sum(li[:i]))//len(li[:i])==(sum(li[i:]))//len(li[i:]):
        a+=1
        break
    else:
        a=0
if a>=1:
    print("yes")
else:
    print("no")
