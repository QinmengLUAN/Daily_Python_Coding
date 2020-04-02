"""
Leetcode1306. Jump Game III
Medium: Moe's improved version. BFS, while loop.

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
		curr_layer = set()
		curr_layer.add(start)
		visited = set()
		while len(curr_layer) > 0:
			next_layer = set()
			for position in curr_layer:
				if arr[position] == 0:
					return True
				visited.add(position)
				next_position_left = position + arr[position]
				next_position_right = position - arr[position]
				if 0 <= next_position_left < len(arr) and next_position_left not in visited:
					next_layer.add(next_position_left)
				if 0 <= next_position_right < len(arr) and next_position_right not in visited:
					next_layer.add(next_position_right)
				curr_layer = next_layer
		return False

arr = [2,1,0]
start = 2
s = Solution()
print(s.canReach(arr, start))
