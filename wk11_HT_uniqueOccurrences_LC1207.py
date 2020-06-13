"""
1207. Unique Number of Occurrences
Easy: Hash Table

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_counter = Counter(arr)
        arr_unique = set(arr_counter.values())
        return len(arr_counter) == len(arr_unique)
    
    
    def uniqueOccurrences1(self, arr: List[int]) -> bool:
        arr_counter = Counter(arr)
        # print(arr_counter)
        appeared_occur = set()
        for item in set(arr):
            if arr_counter[item] in appeared_occur:
                return False
            else:
                appeared_occur.add(arr_counter[item])
        return True