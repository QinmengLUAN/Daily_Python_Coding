"""
Leetcode1306. Jump Game III
Medium: Recursion solution, DFS, check wk6_canReach_v4.py for the revised recursion version.

Given an array of non-negative integers arr, 
you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], 
check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
"""
class Solution:
	def canReach_helper(self, arr, start, visited):
		curr_layer = set()
		curr_layer.add(start)
		next_layer = set()

		if arr[start] == 0:
			return True
		visited.add(start)
		if 0 <= (start + arr[start]) < len(arr) and (start + arr[start]) not in visited:
			next_layer.add(start + arr[start])
		if 0 <= (start - arr[start]) < len(arr) and (start - arr[start]) not in visited:
			next_layer.add(start - arr[start])
		curr_layer = next_layer
		# print(curr_layer)
		# print(visited)

		if len(curr_layer) == 0:
			return False
		else:
			for item in curr_layer:
				if self.canReach_helper(arr, item, visited):
					return True

	def canReach(self, arr, start):
		visited = set()
		return self.canReach_helper(arr, start, visited)

arr = [4,4,1,3,0,3]
start = 2

s = Solution()
print(s.canReach(arr, start))
