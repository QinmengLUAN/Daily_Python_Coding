"""
1346. Check If N and Its Double Exist
Easy: Array

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        double_set = set()
        for i in range(len(arr)):
            if arr[i] in double_set:
                return True
            if arr[i] % 2 == 0:
                double_set.add(arr[i] // 2)
            double_set.add(arr[i] * 2)
        return False