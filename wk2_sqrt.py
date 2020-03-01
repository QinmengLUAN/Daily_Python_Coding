# Write a function to calculate the result (integer) of sqrt(num)
# Cannot use the build-in function
# Method: binary search

def my_sqrt(num):
	left_boundary = 0
	right_boundary = num

	if num <= 0:
		return False
	elif num < 1:
		return 0
	elif num == 1:
		return num
	
	while (right_boundary - left_boundary) > 1:
		mid_num = (right_boundary + left_boundary) // 2 #Update mid_num
		new_num = mid_num * mid_num
		if new_num < num:
			left_boundary = mid_num
		elif new_num > num:
			right_boundary = mid_num
		elif new_num == num:
			return mid_num

	return left_boundary
#Input: 
a = 15

print(my_sqrt(a))
