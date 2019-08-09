r,v=map(int,input().split())
l=[]
a=0
for i in range(r):
    l.append(input())
for i in range(r):
    for j in range(v-1):
        if l[i][j]=="S" and l[i][j+1]=="D":
            c=a+5
        elif l[i][j]=="D" and l[i][j+1]=="D":
            c=c+3
print(c)
