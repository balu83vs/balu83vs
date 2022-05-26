n = int(input())
s = ''
s1 = ''
temp = 0
while n != 0:
    temp = n // 2
    if n % 2 == 1:
        s += '1'
    else:
        s += '0'
    n = temp
for i in range(len(s)-1, -1, -1):
    s1 = s1 + s[i]
print(s1)
