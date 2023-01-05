'''
Palindrome number
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
'''

def palindrome(n):
    pln=n[::-1]
    if n==pln:
        print("it's a palindrome")
        return True
    else:
        print("Sorry!! it's  not a palindrome")
        return False

n=input()
palndrm=palindrome(n)
print(palndrm)
