"""
227. Basic Calculator II
Medium: String

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
class MySolution:
    def calculate(self, s: str) -> int:
        outer = ["+"] + re.split('([+-])', s)
        res = 0
        for o in range(len(outer)-1):
            tmp = 1
            if outer[o+1] != "+" and outer[o+1] != "-":
                inner = ["*"] + re.split("([*/])", outer[o+1])
            else:
                inner = re.split("([*/])", outer[o+1])
            for i in range(len(inner)-1):
                if inner[i] == "*" or inner[i] == "/":
                    tmp = tmp*int(inner[i+1]) if inner[i] == '*' else tmp//int(inner[i+1])
            if outer[o] == '+' or outer[o] == '-':
                res += tmp if outer[o] == '+' else -tmp
            # print(res)
        return res
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        outer = iter(['+'] + re.split('([+-])', s))
        for addsub in outer:
            inner = iter(['*'] + re.split('([*/])', next(outer)))
            # print(list(inner))
            term = 1
            for muldiv in inner:
                n = int(next(inner))
                term = term*n if muldiv == '*' else term//n
                # print(term)
            total += term if addsub == '+' else -term
        return total   