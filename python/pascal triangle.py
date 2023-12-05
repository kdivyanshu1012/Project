rows = int(input("enter no. of rows: "))
k = 1
for i in range(1,rows+1):
    for a in range(rows,i,-1):
        print(" ", end="")
    for j in range(0,i):
        if(j == 0 or i ==j):
            k = 1
        else:
            k = k*(i-j)//j
        print(k,end="")
    print()

