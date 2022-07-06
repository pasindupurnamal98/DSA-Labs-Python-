#insertion sort
A=[]

for x in range(10):
    A.append(input("Enter Number: "))
    
print(A)

def insertSort(A):
    for i in range(len(A)):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key
    return A

insertSort(A)
print("Sorted Array: ")
for k in range(len(A)):
    print(A[k])