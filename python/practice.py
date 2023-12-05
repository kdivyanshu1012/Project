a = int(input("Enter Rows: "))
b = int(input("Enter Columns: "))
matrix = []
for i in range(a):
    z = []
    for j in range(b):
        c = int(input(f"enter number {j+1} for row {i+1} of the matrix: "))
        z.append(c)
    matrix.append(z)
for i in range(a):
    for j  in range(b):
        print(matrix[i][j],end="\t")
    print()
transpose = []


for i in range(b):
    t = []
    for j in range(a):
        t.append(matrix[j][i])
    transpose.append(t)  
print("Transpose: ")
for i in transpose:
    for j in i:
        print(j,end="\t")
    print()





