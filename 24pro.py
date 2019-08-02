m=int(input())
c=2**y
mc=[]
for i in range(0,c):
    l=bin(i)[2:].zfill(m)
    if(len(l)<len(bin(2**m-1)[2:])):
        mc.append([l.count("1"),l])
    else:
        mc.append([l.count("1"),l])
mc.sort()
for i in range(len(mc)):
    print(mc[i][1])
