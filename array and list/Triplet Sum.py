"""
Triplet Sum
You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.
Note :
Given array/list can contain duplicate elements.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
"""
from sys import stdin 
def findTriplet(arr, n, x) :
    numTriplets = 0 
    for i in range(n) : 
        for j in range((i + 1), n) :
            for k in range((j + 1), n) : 
                if (arr[i] + arr[j] + arr[k]) == x :
                    numTriplets += 1 
    return numTriplets 
def takeInput() :
    n = int(input())
    if n == 0 : 
        return list(), 0
    arr = list(map(int, input().strip().split(" ")))
    return arr, n 
t = int(input().strip())
while t > 0 :
    arr, n = takeInput()
    x = int(input().strip()) 
    print(findTriplet(arr, n, x))
    
    t -= 1