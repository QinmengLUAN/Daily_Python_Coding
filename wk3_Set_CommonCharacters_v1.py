# Leetcode 1002. Find Common Characters
"""
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings 
within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""
# Use set, intersection
# Drawback: it doesn't work for 
#Input: ["bella","label","roller"]
#Output: ["e","l","l"]

class Solution:
    def commonChars(self, A):
        length = len(A)
        a_list = set(list(A[0]))
        
        for i in range(1,length):
            b_list = set(list(A[i]))
            a_list = a_list.intersection(b_list)
            
        return list(a_list)

s = Solution()
inp = ["cool","lock","cook"]
print(s.commonChars(inp))
