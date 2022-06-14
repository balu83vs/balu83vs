# put your python code here
def matrix_pro(n, matrix1, matrix2):    
    matrix3 = [[0] * n for _ in range(n)]
    sum = 0
    for k in range(n):
        for l in range(n):
            for i in range(n):
                sum += matrix2[k][i] * matrix1[i][l]
            matrix3[k][l] = sum
            sum = 0
    return matrix3

matrix1 = list()
matrix2 = list()

n = int(input())

for _ in range(n):
    temp = [int(ch) for ch in input().split()]
    matrix1.append(temp)
    temp = []
    
matrix2 = matrix1.copy() 
    
m = int(input())

for _ in range(m - 1):    
    matrix2 = matrix_pro(n, matrix1, matrix2).copy()
       
for i in range(n):
    print(*matrix2[i])    
