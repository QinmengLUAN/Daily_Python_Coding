"""
650. 2 Keys Keyboard
Medium: DP, decomposition

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
"""
class Solution:
    def minSteps_1(self, n: int) -> int:
        min_steps = {}
        min_steps[1] = 0
        
        for i in range(2, n+1):
            min_steps[i] = i
            for j in range(2, i//2):
                if i % j == 0:
                    min_steps[i] = min(min_steps[j] + i//j, min_steps[i])       
        # print(min_steps)    
        return min_steps[n]


class Solution:
    def minSteps_2(self, n: int) -> int:
        res = 0
        i = 2
        while i <= n:
            if n % i == 0:
                res += i
                n = n // i
            else:
                i += 1    
        return res