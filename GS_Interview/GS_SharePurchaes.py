"""
GS Share Purchases:
2020 OA
https://leetcode.com/discuss/interview-question/365452/goldman-sachs-oa-2020-shares-purchase
"""
"""
Example 1:

Input: "ABC"
Output: 1
Example 2:

Input: "ABCCBA"
Ouput: 7
Example 3:

Input: "PQACBA"
Output: 7
"""
from collections import deque
class Solution:
    def SharePurchases(self, st):
        res = 0
        dic = {"A": 0, "B": 0, "C": 0}
        dq = deque()

        for i in range(len(st)):
            if st[i] in dic:
                dic[st[i]] += 1
                dq.append((st[i], i))

                while len(dq) > 0 and dic[dq[0][0]] > 1:
                    dic[dq[0][0]] -= 1
                    dq.popleft()
            if min(dic.values()) > 0:
                res += dq[0][1] + 1
        return res

    def SharePurchases1(self, st):
        res = 0
        dic = {"A":[], "B":[], "C":[]}
        s = len(st)

        # added in reverse order to allow pop() to be O(1)
        for i in range(s-1, -1, -1):
            if (st[i] in dic.keys()):
                dic[st[i]].append(i)
        # print(dic)
        for i in range(s):
            index = list(map(lambda x:x[-1], dic.values()))
            min_idx = min(index)
            max_idx = max(index)
            res += (s - max_idx)
            print(res, max_idx)
            if i == min_idx:
                if dic['A'][-1] == min_idx:
                    dic['A'].pop()
                    if (len(dic['A']) == 0):
                        break
                elif dic['B'][-1] == min_idx:
                    dic['B'].pop()
                    if (len(dic['B']) == 0):
                        break
                elif dic['C'][-1] == min_idx:
                    dic['C'].pop()
                    if (len(dic['C']) == 0):
                        break
        return res

inp = "PQACBA"
s = Solution()
print(s.SharePurchases(inp))