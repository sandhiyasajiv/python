sandy=(input())
bb1=0
for i in range(0,len(sandy)):
    vs=(sandy[:i]+sandy[i+1:])
    if(int(vs) % 8==0):
        bb1=1
        break
if(bb1==1):
    print("yes")
else:
    print("no")
