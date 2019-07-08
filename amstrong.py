p1=int (input())
sum=0
a=p1
while a>0:
  digit=a%10
  sum+=digit**3
  a//=10
if p1==sum:
    print("yes")
else:
    print("no")     
