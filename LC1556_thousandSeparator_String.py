"""
1556. Thousand Separator
Easy: String

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = deque()
        idx = 0
        while n > 0:
            if idx >= 3:
                res.appendleft(".")
                idx = 0
            idx += 1
            r = n % 10
            res.appendleft(str(r))
            n = n // 10
        if len(res) == 0:
            return "0"
        return "".join(res)