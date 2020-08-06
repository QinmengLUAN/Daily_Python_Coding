"""
977. Squares of a Sorted Array
Easy: Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = deque()
        l, r = 0, len(A) - 1
        
        if A[l] > 0:
            return [A[i]**2 for i in range(len(A))]
        elif A[r] <= 0:
            return [A[i]**2 for i in range(len(A) - 1, -1, -1)]
        
        while l <= r:
            if A[l]**2 <= A[r]**2:
                res.appendleft(A[r]**2)
                r -= 1
            else:
                res.appendleft(A[l]**2)
                l += 1
        return res
                
  def sortedSquares2(self, A: List[int]) -> List[int]:           
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
#         return A