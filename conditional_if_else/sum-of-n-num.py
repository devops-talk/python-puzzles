"""
Sum of n numbers
Given an integer n, find and print the sum of numbers from 1 to n.
"""
n=int(input())
sum=0
while n>=1:
    sum=sum+n
    n=n-1
print(sum)