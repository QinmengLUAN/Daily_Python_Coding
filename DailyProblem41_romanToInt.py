"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.

Example:
Input: IX
Output: 9

Input: VII
Output: 7

Input: MCMIV
Output: 1904
Roman numerals are based on the following symbols:
I     1
IV    4
V     5
IX    9 
X     10
XL    40
L     50
XC    90
C     100
CD    400
D     500
CM    900
M     1000

Numbers are strings of these symbols in descending order. 
In some cases, subtractive notation is used to avoid repeated characters. 
The rules are as follows:
1.) I placed before V or X is one less, so 4 = IV (one less than 5), and 9 is IX (one less than 10)
2.) X placed before L or C indicates ten less, so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
3.) C placed before D or M indicates 100 less, so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).

class Solution():
  def romanToInt(self, s):
    # Fill this in.
    
n = 'MCMX'
print(Solution().romanToInt(n))
# 1910
"""
"""
Algorithm to convert Roman Numerals to Integer Number:  

1. Split the Roman Numeral string into Roman Symbols (character).
2. Convert each symbol of Roman Numerals into the value it represents.
3. Take symbol one by one from starting from index 0: 
    1. If current value of symbol is greater than or equal to the value of next symbol, 
    then add this value to the running total.
    2. else subtract this value by adding the value of next symbol to the running total.
"""
class Solution():
  def romanToInt(self, s):
    convert = {"0": 0, "I":1,"V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
    s += "0"
    ans = 0
    for i in range(len(s) - 1):
        if convert[s[i]] < convert[s[i+1]]:
            ans -= convert[s[i]]
        else:
            ans += convert[s[i]]
    return ans
    
n = 'MCMX'
print(Solution().romanToInt(n))
# 1910