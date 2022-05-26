n = int(input())
a1 = 0
a2 = 1
print(a2)
for i in range(1,n):
    s = a1 + a2
    a1 = a2
    a2 = s
    print(s)
