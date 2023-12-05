n = int(input("enter last number: "))
z = n
a = "*"
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
while(z>0):
    print(a * z)
    z-=1
    
