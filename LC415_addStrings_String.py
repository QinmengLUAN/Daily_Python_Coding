"""
415. Add Strings
Easy: String

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Accepted
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = "0" * (len(num1) - len(num2)) + num2
        elif len(num2) > len(num1):
            num1 = "0" * (len(num2) - len(num1)) + num1
        
        res = []
        array = 0
        for i in range(len(num1) - 1, -1, -1):
            val = int(num1[i]) + int(num2[i]) + array
            res.append(str(val % 10))
            array = val // 10
        if array != 0:
            res.append(str(array))
        # print(res)
        return "".join(reversed(res))