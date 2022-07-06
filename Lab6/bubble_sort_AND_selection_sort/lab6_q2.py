#bubble sort
A=[]
for v in range(8):
    A.append(input("Enter Number: "))
print(A)

#IMP
def bubblesort(A):
    for i in range(0,len(A)):
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
                
#CALLING FUNCTION
bubblesort(A)
print("Sorted Array: ")
print(A)                