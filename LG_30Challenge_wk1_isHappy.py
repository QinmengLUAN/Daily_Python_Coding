"""
30 days Leetcode Challenge
wk1: isHappy
Leetcode202, recursion
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
class Solution:
	def isHappy(self, n):
		appeared = set()
		appeared.add(0)
		return self.helper(n, appeared)

	def helper(self, n, appeared):
		if n == 1:
			return True
		elif n not in appeared:
			appeared.add(n)
		elif n in appeared:
			return False
		digit_list = []
		while n > 0:
			digit_list.append(n % 10)
			n = n // 10
		for item in digit_list:
			n += (item * item)
		return self.helper(n, appeared)

n = 2
s = Solution()
print(s.isHappy(n))
