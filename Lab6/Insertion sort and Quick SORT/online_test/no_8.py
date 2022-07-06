def sum(n):
    if n == 1:
        return 1
    else:
        return (sum(n - 1) + n)
    
while True:
    n = int(input("Please Enter Number: "))
    if n == -1:
        break
    print("The result is: ",sum(n))    
    