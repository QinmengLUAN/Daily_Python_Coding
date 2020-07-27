# Solution 1: use list to store appeared times
class Solution1:
    def MaximalCommonality(self, stri):
        count = [0 for _ in range(26)]
        for i in stri:
            count[ord(i) - 97] += 1

        res = 0
        cur = 0
        for i in stri:
            if count[ord(i) - 97] > 1:
                cur += 1
                count[ord(i) - 97] -= 2
            elif count[ord(i) - 97] == 0:
                cur -= 1
            res = max(cur, res)
        return res

# Solution 2: use Counter
from collections import Counter
class Solution:
    def MaximalCommonality(self, stri):
        count = Counter(stri)
        res = 0
        cur = 0
        for i in stri:
            if count[i] > 1:
                cur += 1
                count[i] -= 2
            elif count[i] == 0:
                cur -= 1
            res = max(cur, res)
        return res

s = Solution()
inp = "abcdedear"
inp = "abcdecdefg"
inp = "aaaa"
# inp = "abcabca"
# inp = "aaa"
print(s.MaximalCommonality(inp))