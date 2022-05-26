# put your python code here
temp = list()
xy_list = list()
n = int(input())
for i in range(n):
    xy_string = input()
    temp = xy_string.split(' ')
    xy_list.extend(temp)
print(xy_list)
