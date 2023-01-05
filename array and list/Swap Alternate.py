"""
Swap Alternate
You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
You don't need to print or return anything, just change in the input array itself.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
"""
def swapAlternate (li):
    length =len(li)
    i = 0
    for k in range(length//2):
        li[i],li[i+1]=li[i+1],li[i]
        i+=2
    print(*li,end=" ")
    print()

loop_cycle=int(input())
for i in range(0, loop_cycle):
    faltu = input()
    lip = [int(x) for x in input().split()]
    swapAlternate(lip)