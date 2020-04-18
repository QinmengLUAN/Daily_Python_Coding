"""
1299. Replace Elements with Greatest Element on Right Side
Easy: Array, In-place

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""
class Solution:
    def replaceElements(self, arr):          
        i = len(arr) - 1
        new_max = temp_max = arr[i]
        arr[i] = -1
        i -= 1
        while i >= 0:
            new_max = max(arr[i], new_max)
            arr[i] = temp_max
            temp_max = new_max
            i -= 1 
        return arr

arr = [17,18,5,4,6,1]
s = Solution()
print(s.replaceElements(arr))