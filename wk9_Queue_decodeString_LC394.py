"""
394. Decode String
Medium: Stack, DFS

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ""

        for item in s:
            if item == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0

            elif item == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString 

            elif item.isdigit():
                curNum = curNum * 10 + int(item)

            else:
                curString += item
        return curString


s = Solution()
stri= "3[a2[c]]"
print(s.decodeString(stri))