"""
Reverse of a number

Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
"""
N=input()
rev=N[::-1]
final_rev=rev.lstrip("0")
print(final_rev)