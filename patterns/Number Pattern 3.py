"""
Number Pattern 3
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221
"""
n = int(input())



i=1

while i<=n:
    j=1
    while j<=i:
        if(j==1 or j>=i):
            print('1',end='')
        else:
            print('2',end='')
        j=j+1
    print()
    i=i+1

