"""
Sum of even & odd
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
"""

N = int(input())
Sum_of_Even_Digits=0
Sum_of_Odd_Digits=0
for i in range(0,N+1):
    if i%2==0:
        Sum_of_Even_Digits=Sum_of_Even_Digits+i
    else:
        Sum_of_Odd_Digits=Sum_of_Odd_Digits+i
print(Sum_of_Even_Digits,Sum_of_Odd_Digits)