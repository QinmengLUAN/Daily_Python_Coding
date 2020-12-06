"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will contain only lower-case letters.

Example:
Input: ["daily", "interview", "pro", "pro", 
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
class Solution(object):
  def topKFrequent(self, words, k):
    # Fill this in.

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
"""
from collections import Counter
class Solution(object):
  def topKFrequent1(self, words, k):
        c = Counter(words)
        return [c.most_common(k)[i][0] for i in range(k)]
        
  def topKFrequent(self, words, k):
        c = Counter(words) 
        return sorted(c.keys(), key = lambda x:x[1], reverse=True)[:k]


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']