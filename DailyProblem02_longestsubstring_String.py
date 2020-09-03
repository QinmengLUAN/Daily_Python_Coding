"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

Can you find a solution in linear time?
"""
class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
        if len(s) <= 1:
            return len(s)
        seen = {}
        seen[s[0]] = 0
        
        l, r = 0, 1
        res = 1
        while r < len(s):
            # print(l, r)
            if s[r] not in seen:
                seen[s[r]] = r
                res = max(r-l+1, res)
                r += 1
            else: 
                for k in range(l, seen[s[r]]):
                    if s[k] in seen:
                        del seen[s[k]]
                l = seen[s[r]] + 1
                seen[s[r]] = r
                r += 1
            # print(seen)
        return res

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10