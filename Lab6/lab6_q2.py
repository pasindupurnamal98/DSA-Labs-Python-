#quicksort
arr=[]
for v in range(6):
    arr.append(input("Enter Number: "))
    print(arr)
    
def partition(A,p,r):
    pivot=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=pivot:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    return A  
quicksort(arr,0,len(arr)-1)
print("Sorted Array: ")
for i in range(len(arr)):
    print(arr[i])      