a = int(input())
list1 = []
count=1
for i in range(1,a):
    s = input()
    list1.append(s)
list1.sort()
start=list1[1]
end=list1[a-2]
for i in range(0,10000):
    if(start[1:i]==end[1:i]):
        count=count+1
    else:
        break
print(start[1:count-1])
