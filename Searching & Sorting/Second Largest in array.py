



def print2largest(arr,
                  arr_size):
  
 
  if (arr_size < 2):  
    print(" Invalid Input ")
    return
  

  arr.sort
  
  
  for i in range(arr_size-2, -1, -1):
    if (arr[i] != arr[arr_size - 1]) :
        print("The second largest element is",arr[i])
    return
  
  print("There is no second largest element")
 
# Driver code
arr = [int(x) for x in input().split()]
n = len(arr)
print2largest(arr, n)