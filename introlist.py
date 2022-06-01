# put your python code here
mylist = []
mylist2 = []
ver = []
mylist = input().split(' ')
ver.append(mylist[0])
for i in range(1, len(mylist)):
    if ver[-1] == mylist[i]:
        ver.append(mylist[i])
    else:
        mylist2.append(ver)
        ver = []
        ver.append(mylist[i])
        #mylist2.append(ver)
mylist2.append(ver)
print(mylist2)
