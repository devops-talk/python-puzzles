"""
Number Pattern 2
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
"""
n = int(input())

print(1)

i=1

while i<=n-1:
    j=1
    while j<=i+1:
        if(j==1 or j>=i+1):
            print(i,end='')
        else:
            print('0',end='')
        j=j+1
    print()
    i=i+1