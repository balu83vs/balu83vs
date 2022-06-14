# put your python code here
matrix1 = []
matrix2 = []

sum = 0

n1, m1 = map(int, input().split())
for i in range(n1):
    temp = [int(ch) for ch in input().split()]
    matrix1.append(temp)
    temp = []

input()  

n2, m2 = map(int, input().split())
for i in range(n2):
    temp = [int(ch) for ch in input().split()]
    matrix2.append(temp) 
    temp = []

matrix3 = [[0] * max(m1, m2) for i in range(max(n1, n2))]   

if n1 >= n2 and m2 >= m1:

    for k in range(max(n1, n2)):
        for l in range(max(m1, m2)):
            for i in range(min(n1, n2)):
                sum += matrix1[k][i] * matrix2[i][l]
            matrix3[k][l] = str(sum).rjust(3)
            sum = 0   
    for i in range(max(n1, n2)):
        for j in range(max(m1, m2)):
            print(matrix3[i][j], end = ' ')
        print() 
            
else:
    for k in range(n1):
        for l in range(m2):
            for i in range(n2):
                sum += matrix1[k][i] * matrix2[i][l]
            print(sum)
