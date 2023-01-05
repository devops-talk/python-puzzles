"""
Code : Interesting Alphabets
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
"""
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(64+n-i+j),end="")
        j=j+1
    print("")
    i=i+1
    