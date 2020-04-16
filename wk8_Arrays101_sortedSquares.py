"""
977. Squares of a Sorted Array
Easy: Array, Two Pointer, O(n) time complexity, O(1) space complexity

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
class Solution:
    def sortedSquares(self, A):
        length = len(A)
        left = 0
        right = length - 1
        while left <= right:
            if abs(A[left]) > abs(A[right]):
                poped = A.pop(left)
                A.insert(right,poped)
            else:
                right -= 1    
        for i in range(length):
            A[i] **= 2
        return A

inp = [-4,-1,0,3,10]
s = Solution()
print(s.sortedSquares(inp))