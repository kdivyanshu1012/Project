x  = int(input("Enter Number 1: "))
y  = int(input("Enter Number 2: "))
if(x>y):
    max = x
else:
    max = y
for i in range(1,max+1):
    if(x%i==0 and y%i==0):
        hcf = i
print(f"gcd of {x} and {y} is {hcf}")