# Leetcode 1002. Find Common Characters
# Medium
"""
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings 
within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""
# Use map
# Strength: it works for 
#Input: ["bella","label","roller"]
#Output: ["e","l","l"]

class Solution:
    def commonChars(self, A):
        length = len(A)
        dic_str = [{} for n in range(0,length)] # Important!!!
        new_index = 1
        for i in range(0,length):
        	str_list = list(A[i])
        	for j in range(0,len(str_list)):
        		if str_list[j] not in dic_str[i].keys():
        			dic_str[i].update({str_list[j]: 1})
        		elif str_list[j] in dic_str[i].keys():
        			new_index = dic_str[i].get(str_list[j]) + 1
        			dic_str[i].update({str_list[j]: new_index})

        dic_list = dic_str[0]

        for i in range(1,length):
        	for k in list(dic_list.keys()):
        		if k not in list(dic_str[i].keys()):
        			dic_list.pop(k)
        		else:
        			if dic_str[i].get(k) < dic_list.get(k):

        				dic_list.update({k:dic_str[i].get(k)})
        result = []
        for k in dic_list.keys():
        	num = dic_list.get(k)
        	for i in range(num):
        		result.append(k)
        return result


s = Solution()
inp = ["cooll","loockl","cookl"]
print(s.commonChars(inp))
