
def checknum(number):
    if(len(number)==11 ):
        increment = 0
        for i in number:
            if(i.isdigit()==True and increment!=5):
                print("Number Is Valid")
            elif(increment==5 and i=='-'):
                print("Number Is Valid")
                
    else:
        print("Number Invalid")

number = input("Enter Your Number")

checknum(number)



