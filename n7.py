
x=int(input())
y=0
for i in range(0,x):
  if(pow(2,i)>x):
    break
  y=x-pow(2,i)
print(y)
