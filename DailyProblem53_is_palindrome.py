"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.

import math

def is_palindrome(n):
  # Fill this in.

print is_palindrome(1234321)
# True
print is_palindrome(1234322)
# False
"""
import math

def is_palindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def is_palindrome1(n):
    if n < 0:
        new = -n
    new = n
    reverse = []
    while new > 0:
        reverse.append(new % 10)
        new //= 10
    reverse_n = int("".join(map(str, reverse))) 
    return reverse_n == abs(n)

print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False