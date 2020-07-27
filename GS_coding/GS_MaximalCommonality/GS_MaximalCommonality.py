from collections import Counter
class Solution:
    def MaximalCommonality(self, s):
        c = Counter(s)
        cnt = 0

        for ch in s:
            c[ch] -= 1
            if c[ch] > 0:
                cnt += 1
        return cnt

s = Solution()
inp = "abcdedear"
inp = "abcdecdefg"
inp = "aaaa"
inp = "abcabca"
print(s.MaximalCommonality(inp))