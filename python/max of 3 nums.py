a,b,c = map(int,input("enter no").split())
if(a>b and b>c):
    print("a: ",a)
elif(b>c and c>a):
    print("b: ",b)
elif(c>a and a>b):
    print("c: ",c)
else:
    print("all equal")