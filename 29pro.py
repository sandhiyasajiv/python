s=int(input())
t=[]
for i in range(2,s):
    rev=1
    temp=i
    while temp!=1:
        re=temp%20
        rev=rev+re
        temp=temp//20
    if i+rev==s:
        t.append(i)
print(len(t))
for j in range(0,len(t)):
    print(t[j])
