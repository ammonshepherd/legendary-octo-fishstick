matrixA = []
matrixB = []
matrixC = []


# Type your code here.
matrixA = input().split()

for n in range(len(matrixA)):
    matrixB.append(input().split())
    
for b in range(len(matrixB[0])):
    sum = 0
    for i in range(len(matrixA)):
        sum = sum + (int(matrixA[i]) * int(matrixB[i][b]))
    matrixC.append(sum)

for c in matrixC:
    print(c, end=' ')
print()