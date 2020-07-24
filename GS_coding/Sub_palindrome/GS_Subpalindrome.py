"""
Sub palindrome
Given a string s, determine the number of distinct palindromic substring of s
"""
class Solution:
    def countSubstrings(self, s):
        resT = [[False] * len(s) for i in range(len(s))]
        resSet = set()

        for i in range(len(s)):
            resT[i][i] = True
            resSet.add(s[i])
            if i + 1 < len(s) and s[i] == s[i+1]:
                resT[i][i+1] = True
                resSet.add(s[i:i+2])


        for j in range(2, len(s)):
            for i in range(len(s) - 2):
                if resT[i+1][j-1] == True and s[i] == s[j]:
                    resT[i][j] = True
                    resSet.add(s[i:j+1])
        print(resSet)
        # print(resT)
        return len(resSet)

inp = "aaabbb"
inp = "aaab"
inp = "aabb"
inp = "aba"
s = Solution()
print(s.countSubstrings(inp))