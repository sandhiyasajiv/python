e=int(input())
if e > 1:
    for a in range(3,e):
        if(e%a==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
