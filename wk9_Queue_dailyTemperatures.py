"""
739. Daily Temperatures
Medium: Stack, classic
Time Complexity: O(N), 
where N is the length of T and WW is the number of allowed values for T[i]. Each index gets pushed and popped at most once from the stack.
Space Complexity: O(W). 
The size of the stack is bounded as it represents strictly increasing temperatures.

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        i = len(T) -1
        stack = [i] # store the index with values that are larger than the current idx
        i -= 1
        while i >= 0:
            while len(stack) != 0 and T[i] >= T[stack[-1]]:         
                stack.pop()
            if len(stack) != 0:
                res[i] = stack[-1] - i
            stack.append(i)
            # print(stack, i)
            i -= 1
        return res

T = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
print(s.dailyTemperatures(T))