s=int(input())
r=list(map(int,input().split()))
ans=int(s/3)
rs=s[:ans]
rs=s[ans::]
if ((sum(rs)//len(rs))==(sum(rs)//len(rs))):
    print("yes")
else:
    print("no")
