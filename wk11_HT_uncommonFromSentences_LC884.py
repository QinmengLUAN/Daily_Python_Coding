"""
884. Uncommon Words from Two Sentences
Easy

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""
class Solution:
# Method 1: do not use package
    def uncommonFromSentences1(self, A, B):
    # Explanation:
    # Two steps:
    # Count words occurrence to a HashMap<string, int> count.
    # Loop on the hashmap, find words that appears only once.
        C = (A + " " + B).split()
        C_dic = {}
        
        for item in C:
            if item not in C_dic:
                C_dic[item] = 1
            else:
                C_dic[item] += 1
                
        res = []
        # print(C_dic)
        for jtem in C_dic:
            if C_dic[jtem] == 1:
                res.append(jtem)
        return res

# Solution 2: use collection.Counter package
    def uncommonFromSentences(self, A, B):
        C = Counter((A + " " + B).split())
        return [item for item in C.keys() if C[item] == 1]

A = "this apple is sweet"
B = "this apple is sour"
s = Solution()
print(s.uncommonFromSentences(A, B))



