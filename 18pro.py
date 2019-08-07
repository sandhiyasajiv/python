dert,art=map(int,input().split())
l1=[]
for _ in range(dert):
    l1.append(input())
for ic in range(len(l1)):
    if('0' in l1[ic]):
        l1[ic]=l1[ic].replace('0','')
    l1[ic]=l1[ic].replace(' ','')
lengths=[]
for ic in l1:
    if(len(ic)>3):
        lengths.append(len(ic))
art=min(lengths)
r2='1 '*art
r2=r2.strip()
for ic in range(art):
    print(r2)
