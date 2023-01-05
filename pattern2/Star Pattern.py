'''
Print the following pattern
Pattern for N = 4
   *
  ***
 *****
*******

The dots represent spaces.
'''
n=int(input())
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    k=1
    while k<=i-1:
        print("*",end="")
        k=k+1
    print("")
    i=i+1