def Multiply(m,n):
    if(n==1):
        return m
    else:
        return (m + Multiply(m,n-1))
    
while True:
    no1=int(input("Please Enter No1: "))
    no2=int(input("Please Enter No2: "))
    if(no1==-1 and no2==-1):
         break
         
    print("The result is: ",Multiply(no1,no2))

            