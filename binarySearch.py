import math
def binarySearch(A,minn,maxx,key):
    if maxx < minn:
        return False
    
    else:
        mid =math.floor((minn+maxx)/2)
        
        if A[mid]<key:
            return binarySearch(A,mid+1,maxx,key)
        elif A[mid]>key:
            return binarySearch(A,minn,mid-1,key)
        else:
            return mid
            
            

B=[12,23,34,56,76,86]
print(binarySearch(B,0,len(B),34))
