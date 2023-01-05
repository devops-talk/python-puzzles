"""
Fahrenheit to Celsius Function
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
Input Format :
3 integers - S, E and W respectively
"""
def printTable(start,end,w):
    for i in range(s,e+1,w):
        C = int(5/9 * (i-32))
        print(i,C)



s = int(input())
e = int(input())
w = int(input())

printTable(s,e,w)