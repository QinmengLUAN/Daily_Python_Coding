"""
1380. Lucky Numbers in a Matrix
Given a m * n matrix of distinct numbers, 
return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix 
such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
"""

def luckyNumbers(inp):
	lucky = []
	rows = len(inp)
	cols = len(inp[0])

	for i in range(rows):
		min_row = inp[i][0]
		for j in range(cols):
			if inp[i][j] <= min_row:
				i_idx = i
				j_idx = j			
			min_row = min(min_row, inp[i][j])
		max_col = min_row
		for k in range(rows):
			max_col = max(max_col, inp[k][j_idx])
			print(min_row)
		if min_row == max_col:
			lucky.append(min_row)
	return lucky

"""
inp = [[3,7,8],[9,11,13],[15,16,17]]
print(luckyNumbers(inp))

inp = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(luckyNumbers(inp))
"""
inp = [[7,8],[1,2]]
print(luckyNumbers(inp))