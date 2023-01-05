"""
Check Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters.
Palindrome
A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.
Example:
If the input string happens to be, "malayalam" then as we see that this word can be read the same as forward and backwards, it is said to be a valid palindrome.

The expected output for this example will print, 'true'.
"""
first_string=input("").strip()
#second_string=first_string[::-1]
if first_string==first_string[::-1]:
    print("true")
else:
    print("false")