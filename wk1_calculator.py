"""
write a calculator

"""
class Solution:
	def calculator(self, num_str):
		number = num_str.split()
		new_list = []
		#number = num_str
		i = 0
		while i < len(number):
			if number[i] != "*":
				new_list.append(number[i])
			else:
				left_num = new_list.pop()
				right_num = number[i + 1]
				new_num = int(left_num) * int(right_num)
				new_list.append(new_num)
				i += 1
			i += 1
		print(new_list)

		total = int(new_list[0])

		for t in range(1,len(new_list)):
			if new_list[t-1] == "+":
				total = total + int(new_list[t])
			elif new_list[t-1] == "-":
				total = total - int(new_list[t])
		return total



	def calculator_2(self, num_str):
		reverse_list = ""
		#reverse_list = reverse_list.append(num_str[0])
		for i in range(0,len(num_str)):
			if num_str[i] != "+" and num_str[i] != "-" and num_str[i] != "*":
				reverse_list = reverse_list + num_str[i]
			else:
				reverse_list = reverse_list + " "
				reverse_list = reverse_list + num_str[i]
				reverse_list = reverse_list + " "
		return self.calculator(reverse_list);
# testing
"""
p = "11 + 1 - 6 * 5 * 2"
solution = Solution()
print(solution.calculator(p))

p_2 = "11 + 1 - 6* 5*2 -222"
solution = Solution()
print(solution.calculator_2(p_2))
"""