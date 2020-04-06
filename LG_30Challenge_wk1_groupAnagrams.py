"""
30 days Leetcode Challenge
wk1: Group Anagrams_map
Leetcode 49
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs):
        str_idx_map = {}
        count = 0
        res = []
        for item in strs:
            sorted_str = "".join(sorted(item))
            if sorted_str not in str_idx_map:
                res.append([])
                str_idx_map[sorted_str] = count
                res[count].append(item)
                count += 1
            else:
                res[str_idx_map[sorted_str]].append(item)
        return res

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))