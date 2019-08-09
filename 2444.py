aaa1=int(input())
ccc1=pow(2,aaa1)
zee1=[]
for i in range(ccc1):  
    mss1=bin(i).replace("0b","")
    zee1.append(mss1.zfill(aaa1))
    zee1.sort(key=(lambda x:x.count('1')))
for i in zee1:
    print(i)
