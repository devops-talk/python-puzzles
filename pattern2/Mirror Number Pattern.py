"""
Code : Mirror Number Pattern
Print the following pattern for the given N number of rows.
Pattern for N = 4
   1
  12
 123
1234
"""
n= int(input())
i =1
while i<=n:
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print("")
    i=i+1