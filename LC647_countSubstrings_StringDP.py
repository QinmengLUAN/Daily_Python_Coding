"""
647. Palindromic Substrings
Medium: String, DP 

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
class Solution:
    # Improved version; table filling from from the bottom
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res

class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        resT = [[False] * len_s for i in range(len_s)]
        dq = deque()
        cnt = 0
        
        for i in range(len_s):
            resT[i][i] = True
            cnt += 1
            dq.append((i,i))
            if i+1 < len_s and s[i] == s[i+1]:
                resT[i][i+1] = True
                cnt += 1
                dq.append((i,i+1))
                
        while len(dq) > 0:
            m,n = dq.popleft()
            if m - 1 >= 0 and n + 1 < len_s:
                if s[m-1] == s[n+1]:
                    resT[m-1][n+1] = True
                    cnt += 1
                    dq.append((m-1, n+1))
        # print(resT)
        return cnt