
def pushZerosToEnd(arr, n):
    count = 0 # Count of non-zero elements
     
 
    for i in range(n):
        if arr[i] != 0:
             
            arr[count] = arr[i]
            count+=1
     
   
    while count < n:
        arr[count] = 0
        count += 1
         
# Driver code
arr = [int(x) for x in input().split()]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)


"""
A = [int(x) for x in input().split()]
n = len(A)
j = 0
for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j]  # Partitioning the array
        j += 1
print(A)
"""