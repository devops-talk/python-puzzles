"""
Find Unique
You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
You need to find and return that number which is unique in the array/list.
 Note:
Unique element is always present in the array/list according to the given condition.
"""
import sys
def findUnique(arr, n) :
    for i in range(n) :
        j = 0
        while j < n :
            if i != j :
                if arr[i] == arr[j] :
                    break
            j += 1
        if j == n : 
            return arr[i]
def takeInput() :
    n = int(input())
    if n == 0 :
        return list(), 0
    arr = list(map(int, input().rstrip().split(" "))) 
    return arr, n
t = int(input()) 
while t > 0 : 
    arr, n = takeInput()
    print(findUnique(arr, n)) 
    t -= 1