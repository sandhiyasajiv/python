vs=int(input())
ks=list(map(int,input().split(" ")))
ks=[bin(j) for j in ks]
ks.sort(reverse=True)
ks=[int(vs,2) for vs in ks]
for i in range(0,vs):
     print(ks[i])
