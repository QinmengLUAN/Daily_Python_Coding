"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
Here is a starting point:

def findKthLargest(nums, k):
  # Fill this in.

print findKthLargest([3, 5, 2, 4, 6, 8], 3)
"""
import heapq
def findKthLargest(nums, k):
    # Fill this in.
    if len(nums) < 3:
        return None
    h = []
    for i in range(3):
        heapq.heappush(h, nums[i])

    for j in range(3, len(nums)):
        heapq.heappush(h, nums[j])
        heapq.heappop(h)

    return heapq.heappop(h)

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))