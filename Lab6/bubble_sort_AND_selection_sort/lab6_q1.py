#selection sort
A=[]
for v in range(6):
    A.append(input("Enter Number: "))
print(A)

#implementation
def selectionsort(A):
    for i in range(0,len(A)-1):
        min=i
        for j in range(i+1,len(A)):
            if A[j]<A[min]:
                min=j
        A[i],A[min]=A[min],A[i]
    return A

#calling function
selectionsort(A)
print("Sorted Array: ")
print(A)