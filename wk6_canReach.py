"""
Leetcode1306. Jump Game III
Medium: Moe's messy version, but works well. BFS.

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
	def canReach(self, arr, start):
		if 0 not in arr:
			return False
		if arr[start] == 0:
			return True

		appeared_idx = set()
		appeared_idx.add(start)
		jump = self.jump_check(arr, [start])
		while len(jump) > 0:
			print(jump)
			if len(jump) == 0:
				return False
			if set(jump).issubset(appeared_idx):
				return False
			star = []
			for i in range(len(jump)):
				if arr[jump[i]] == 0:
					return True
				elif jump[i] not in appeared_idx:
					appeared_idx.add(jump[i])
					star.append(jump[i])
			jump = self.jump_check(arr, star)				
		return False

	def jump_check(self, arr, start):
		jump = []
		for i in range(len(start)):
			if 0 <= (start[i] + arr[start[i]]) < len(arr):
				jump.append(start[i] + arr[start[i]])
			if 0 <= (start[i]- arr[start[i]]) < len(arr):
				jump.append(start[i] - arr[start[i]])
		return jump

arr = [2,1,0]
start = 2
s = Solution()
print(s.canReach(arr, start))
