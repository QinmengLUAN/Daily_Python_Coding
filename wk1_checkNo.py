"""
Check whether a number is appeared in the list

"""
class Solution:
	def checkNo(self, p, inp):

		length = len(p)

		left = 0
		right = length -1
		

		while right != left and abs(right-left) != 1:

			mid = (right+left)//2

			# print(right, left, mid)

			if inp == p[mid]:
				return True

			elif inp > p[mid]:
				left = mid
			else:
				right = mid

		return p[left] == inp or p[right] == inp




p = [1,2,3,4,5,6,7,8,9]
inp = 9

solution = Solution()
print(solution.checkNo(p, inp))