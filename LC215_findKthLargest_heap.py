"""
215. Kth Largest Element in an Array
Medium: Heap
Time complexity: k * O(logN)
Space complexity: O(N)

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""
class Solution:
    # Quick sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = []
        right = []
        equal = []
        pivot = random.choice(nums)
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                right.append(num)
                
        if len(right) == k - 1:
            return pivot
        
        if len(right) > k - 1:
            return self.findKthLargest(right, k)
            
        if len(equal) >= k - len(right):
            return pivot
        
        return self.findKthLargest(left, k - len(right) - len(equal))
            
    # heap
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums:
            heapq.heappush(hq, num)
            if len(hq) > k:
                heapq.heappop(hq)              
        return heapq.heappop(hq)

class Solution:
    # reverse heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for n in nums:
            heapq.heappush(hp, -1 * n)
        for i in range(k):
            val = heapq.heappop(hp)
            if i + 1 == k:
                return -1 * val
