"""
Code : Character Pattern
Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG
"""

n=int(input())

i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(64+i+j-1),end="")
        j=j+1
    print("")
    i=i+1