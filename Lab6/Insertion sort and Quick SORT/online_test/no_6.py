def sumcube(n):
    if n == 1:
        return 1
    else:
        return (sumcube(n - 1) + n * n * n)
    
while True:
    n = int(input("Please Enter Number: "))
    if n == -1:
        break
    print("The result is: ",sumcube(n))    