"""
67. Add Binary
Easy: Math, String

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a
            
        res = []
        arr = 0
        for i in range(len(a) - 1, -1, -1):
            added = arr + int(a[i]) + int(b[i])
            res.append(str(added % 2))
            arr = added // 2
        if arr == 1:
            res.append(str(arr))
        # print(res)
        return "".join(reversed(res))