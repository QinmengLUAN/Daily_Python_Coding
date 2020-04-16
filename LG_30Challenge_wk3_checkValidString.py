"""
678. Valid Parenthesis String
Medium: String, feel 懵逼 at the beginning, O(n) time complexity

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""
class Solution:
    def checkValidString(self, s):
        left_par = 0
        right_par = 0
        star = 0
        i = 0
        # check the string from head to end
        while i < len(s):
            if s[i] == '(':
                left_par += 1
            if s[i] == ')':
                if (left_par + star) <= 0:
                    return False
                left_par -= 1   
            if s[i] == '*':
                star += 1
            i += 1
        # check the list from end to head
        j = len(s) - 1
        star = 0
        while 0 <= j:
            if s[j] == ')':
                right_par += 1
            if s[j] == '(':
                if (right_par + star) <= 0:
                    return False
                right_par -= 1
            if s[j] == '*':
                star += 1
            j -= 1    
        return True
inp = ")(*"
s = Solution()
print(s.checkValidString(inp))
"""
False occured only when there is a single ) where there is no ( or * on the left to match with, or when there is a ( with no ) or * on the right.
This is equal to:
when counting from the left, the number of ) is larger than ( and * . And when counting from the right, the numer of ( is larger than ) and * .
If either occured, then returen True.
"""
