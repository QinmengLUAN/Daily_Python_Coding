"""
354. Russian Doll Envelopes
Hard

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0:
            return 0
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        f = [0] * len(envelopes)
        size = 0
        for w,h in envelopes:
            i, j = 0, size
            while i != j:
                m = i + (j - i)//2
                if f[m] < h:
                    i = m + 1
                else:
                    j = m
            f[i] = h
            size = max(size, i + 1)
        # print(f)
        return size
"""
Trick:
let's suppose the values are given as...
[2,3]
[4,6]
[3,7]
[4,8]

If we Sort this envelopes in a tricky way that Sort the envelopes according to width BUT when the values of height are same, we can sort it in reverse way like this :

[2,3]
[3,7]
[4,8]
[4,6]

Now just Do LIS on the all height values, you will get the answer

Solution:
    # only seek height's LIS (longest increasing subsequence), alike Leetcode Question 300.
    # https://leetcode.com/problems/longest-increasing-subsequence/
    # follow up question, how about 3D cases? since Russian Doll are actually with x,y,z dimensions!

# [2,3], [5,4], [6,4], [6,7], [1,2]
# will be sorted to be: [1,2], [2,3], [5,4], [6,7], [6,4]
# where the answer is: 4 for [1,2], [2,3], [5,4], [6,7]

# [2,3], [5,4], [6,4], [7,1], [8,2], [9,3]
# will be sorted to be: [2,3], [5,4], [6,4], [7,1], [8,2], [9,3]
# where the answer is: 3 for [7,1], [8,2], [9,3]
"""
