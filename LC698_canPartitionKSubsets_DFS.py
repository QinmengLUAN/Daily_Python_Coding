"""
698. Partition to K Equal Sum Subsets
Medium: Backtracking, DFS

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        if sum(nums) % k != 0:
            return False
        if k > len(nums):
            return False
        
        nums.sort(reverse = True)
        visited = [0] * len(nums)
        
        return self.helper_dfs(nums, k, visited, 0, 0, sum(nums) // k)
        
        
    def helper_dfs(self, nums, k, visited, curr_sum, idx, target):        
        if k == 1:
            return True
        
        if curr_sum == target:
            return self.helper_dfs(nums, k-1, visited, 0, 0, target)
        
        for i in range(idx, len(nums)):
            if visited[i] == 0 and (curr_sum + nums[i]) <= target:
                visited[i] = 1
                if self.helper_dfs(nums, k, visited, curr_sum + nums[i], i+1, target):
                    return True
                visited[i] = 0
        return False
"""
Solution:
很容易想到每一个子集和必须为target = sum(nums) / k，如果除不尽，那么一定会返回False。
先模拟出k个子集，对于nums中最后一个数n，将其弹出。遍历k个子集，只要加入n后，这个子集和不超过target，就把它加入这个子集当中，然后带着当前的选择，继续递归搜索nums（此时nums已不包括n）。
重复上述过程，如果nums最后为空，那么说明搜索成功了。
这种方法十分直观，但是速度很慢，不过有一些加速方法可以采用，这里列举其中一些：
k个子集从前到后递归，如果当前的子集和与前一个子集和相同，那么这个子集就不用试了，因为把n放到这个子集和放到前一个子集没有差别。我们只关心能否搜索到，并不关心具体的分配方案。
先把nums排序，并优先先放入最大的元素，这样能减少许多搜索路径。
一旦找到numsi > target，那么就直接返回False。因为如果某一个元素，都超过了target，那么就一定不合题。
复杂度分析：
时间复杂度：O(k ^ N)，其中N时nums的长度，k是子集数。如果采用了优化方案a，则复杂度至少降到O(k ^ (N - k) * k!)，因为一开始会跳过很多和为0的子集，至少前k个元素的搜索次数不超过O(k!)。
空间复杂度：O(N)， 用于函数调用栈。
"""
            