# put your python code here

matrix1 = []
matrix2 = []
matrix3 = []

n, m = map(int, input().split())

#matrix3 = ['0' * m for i in range(n)]

for i in range(n):
    temp = [i for i in map(int,input().split())]
    matrix1.append(temp)
    temp = []
    
input()    

for i in range(n):
    temp = [i for i in map(int,input().split())]
    matrix2.append(temp)
    temp = []    
    
#for i in range(n):    
#    print(*matrix1[i])
#print()
#for i in range(n):
#    print(*matrix2[i])
#print()
#print()

for i in range(n):
    for j in range(m):
        temp.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(temp)
    temp = []
        
for i in range(n):
    print(*matrix3[i])
