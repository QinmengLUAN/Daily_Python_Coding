"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a list of numbers, find the smallest window to sort such that the whole list will be sorted. If the list is already sorted return (0, 0). 
You can assume there will be no duplicate numbers.

Example:
Input: [2, 4, 7, 5, 6, 8, 9]
Output: (2, 4)
Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.

def min_window_to_sort(nums):
  # Fill this in.
  
print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
"""
# Ref: https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/

def min_window_to_sort(nums):
    # Step 1: find the candidate unsorted subarray, i.e. s, e positions
    for s in range(len(nums)-1):
        if nums[s] > nums[s+1]: 
            break
    if s == len(nums)-1:
        return "nums is already sorted"
    
    for e in range(len(nums)-1, -1, -1):
        if nums[e] < nums[e-1]:
            break
    # Step 2 a):Find the minimum and maximum values in arr[s..e]
    max_val = max(nums[s:e+1])
    min_val = min(nums[s:e+1])
    # Step 2 b):Find the first element (if there is any) in arr[0..s-1] 
                # which is greater than min, change s to index of this element
    for i in range(s): 
        if nums[i] > min_val: 
            s = i 
            break
    # Step 3 c) Find the last element (if there is any) in arr[e+1..n-1] 
                # which is smaller than max, change e to index of this element.        
    for i in range(len(nums)-1, e, -1): 
        if nums[i] < max_val: 
            e = i 
            break
    return (s, e)
print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)