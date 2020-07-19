"""
69. Sqrt(x)
Easy: Two Pointer or Newton's Method
Integer square root: https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""
class Solution:
    def mySqrt1(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 1, x
        
        while l < r:
            mid = l + (r - l) //2
            if mid ** 2 > x:
                r = mid
            elif mid ** 2 < x:
                if mid == l:
                    return l
                l = mid
            else:
                return mid
            
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return r