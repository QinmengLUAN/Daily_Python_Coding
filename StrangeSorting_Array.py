"""
Strange Sorting Problem
Sort the strings based on the strange mapping, return the sorted string.
nums = ['12','02','4', '023', '65', '83', '224', '50']
mapping = [2,1,4,8,6,3,0,9,7,5]
Output:
['4', '224', '12', '83', '65', '02', '50', '023']
https://leetcode.com/discuss/interview-question/404304/Goldman-Sachs-or-OA-2020-or-Strange-Sorting-Problem
"""
class Solution:
    def StrangeSorting(self, nums, mapping):
        d = {}
        res = []
        sorted_res = []
        for i in range(len(mapping)):
            d[str(mapping[i])] = str(i)
        # print(d)

        for n in nums:
            curr = ""
            for j in n:
                curr += d[j] 
            res.append([int(curr), n])
        res = sorted(res, key = lambda x: x[0])

        for k in range(len(res)):
            sorted_res.append(res[k][1]) 
        return sorted_res

nums = ['12','02','4', '023', '65', '83', '224', '50']
mapping = [2,1,4,8,6,3,0,9,7,5]

# nums = ['990', '332', '32']
# mapping = [3, 5, 4, 6, 2, 7, 9, 8, 0, 1]
s = Solution()
print(s.StrangeSorting(nums, mapping))