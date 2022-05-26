k = input()
s = 0
for i in range(len(k)):
    if k[i] == '1':
        s += 16 ** ((len(k) - 1) - i)
    elif k[i] == '2':
        s += 2 * (16 ** ((len(k) - 1) - i))
    elif k[i] == 'A':
        s += 10 * (16 ** ((len(k) - 1) - i))
    elif k[i] == 'F':
        s += 15 * (16 ** ((len(k) - 1) - i))    
print(s)
    
