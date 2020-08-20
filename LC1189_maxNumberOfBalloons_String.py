"""
1189. Maximum Number of Balloons
Easy: String, Counter, dictionary

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        return min(cnt[ch]//n for ch, n in Counter('balloon').items())
    
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter("balloon")
        c_text = Counter(text)
        res = len(text)
        for i in c:
            res = min(res, c_text[i]//c[i])
        return res