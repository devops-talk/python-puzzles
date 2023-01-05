"""
Pair Sum
You have been given an integer array/list(ARR) and a number X. Find and return the total number of pairs in the array/list which sum to X.
Note:
Given array/list can contain duplicate elements. 
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
"""

from sys import stdin 
def pairSum(arr, size, x) :
    numPairs = 0
    for i in range(size) :
        for j in range((i+1), size) :
            if arr[i] + arr[j] == x :
                numPairs += 1
    return numPairs 
def takeInput() :
    n = int(input())
    if n == 0 :
        return list(), 0
    arr = list(map(int, input().strip().split(" ")))
    return arr, n
t = int(input()) 
while t > 0 :
    arr, n = takeInput()
    x = int(input())
    print(pairSum(arr, n, x)) 
    
    t -= 1