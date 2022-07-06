#no_4
def power(base,exp):
    if exp == 0:
        return 1
    else:
        return base * power(base,exp-1)
while True:
    base=int(input("Please Enter Base: "))
    exp=int(input("Please Enter Exponent: "))
    if(base==-1 and exp==-1):
        break
    print("The result is: ",power(base,exp))    