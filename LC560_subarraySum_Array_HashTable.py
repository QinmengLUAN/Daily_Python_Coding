"""
560. Subarray Sum Equals K
Medium: Array, Hash Table

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
"""
# Method 1: dictionary
# 首先求出nums的前缀和数组 然后将前缀和数组扫一遍，每扫到一个位置就将答案加上前面(k-prefixSum)出现次数（出现次数可以用dict维护） 再将当前前缀和prefixSum在出现的次数+1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
        	nums[i] += nums[i - 1]
        d, ans = {0 : 1}, 0
        for i in range(len(nums)):
        	if(d.get(nums[i] - k) != None):
        		ans += d[nums[i] - k]
        	if(d.get(nums[i]) == None):
        		d[nums[i]] = 1
        	else:
        		d[nums[i]] += 1
        return ans

# Method 2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        r_dic = {0:[len(nums)]}
        r_val = 0
        for t in range(len(nums) - 1, -1, -1):
            r_val += nums[t]
            if r_val not in r_dic:
                r_dic[r_val] = [t]
            else:
                r_dic[r_val].append(t)
        # print(r_dic)
        
        s_val = 0
        res = 0
        val_need = sum(nums) - k
        for i in range(len(nums)):
            v = val_need - s_val
            if v in r_dic:
                res += sum(idx > i for idx in r_dic[v])
                # for idx in r_dic[v]:
                #     if idx > i:
                #         res += 1
            s_val += nums[i]
        return res
                    
