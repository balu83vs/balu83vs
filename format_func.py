
num = input()
num = num[::-1]
temp = ''

# temp = num[0:3] + ',' + num[3:6] + ',' + num[6:]
for i in range(0, len(num), 3):
    temp = temp + num[i:i+3] + ','
temp = temp[::-1]
print(temp[1:])
