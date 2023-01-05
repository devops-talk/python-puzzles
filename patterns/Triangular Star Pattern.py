"""
Code : Triangular Star Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****
"""


n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i+1
    print("")
    