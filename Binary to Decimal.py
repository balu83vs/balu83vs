k = input()
s = 0
for i in range(len(k)):
    if k[i] == '1':
        s += 2 ** ((len(k) - 1) - i)
print(s)
    
