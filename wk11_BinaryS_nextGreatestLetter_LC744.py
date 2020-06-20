"""
744. Find Smallest Letter Greater Than Target
Easy: Binary search

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if len(letters) < 1:
            return None
        
        l, r = 0, len(letters) - 1
        if letters[r] <= target:
            return letters[0]
        if letters[l] > target:
            return letters[0]
        
        while r - l > 1:
            # print(l, r)
            mid = l + (r - l) // 2
            if letters[mid] <= target:
                l = mid
            elif letters[mid] > target:
                r = mid
            
        return letters[r]