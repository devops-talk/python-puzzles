'''
Binary Pattern
Print the following pattern for the given number of rows.
Pattern for N = 4
1111
000
11
0
'''
n =int(input())
i =1
while i<=n:
    j=1
    while j<=n-i+1:
        if i%2!=0:
            print("1",end="")
        else:
            print("0",end="")
        j=j+1
    print("")
    i=i+1