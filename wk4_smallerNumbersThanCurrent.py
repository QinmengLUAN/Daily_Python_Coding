"""
Leecode 1365. How Many Numbers Are Smaller Than the Current Number
"Moe doesn't like this question"
Given the array nums, 
for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] 
you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

"""
def smallerNumbersThanCurrent(nums):
	tup = []
	for i in range(0, len(nums)):
		tup.append([nums[i], i])

	tup.sort(key = lambda tup: tup[0])  # sorts in place

	new_tup = [[0,tup[i][1]] for i in range(len(nums))]
	
	t = 0
	for i in range(1, len(nums)):
		print(i)
		if tup[i][0] == tup[i - 1][0]:
			new_tup[i][0] = t
		else:
			t = i
			new_tup[i][0] = t
	new_tup.sort(key = lambda tu: tu[1])
	
	output = [new_tup[i][0] for i in range(len(nums))] 
	print(output)
	return output


inp = [8,1,2,2,3]
smallerNumbersThanCurrent(inp)
inp2 = [6,5,4,8]
smallerNumbersThanCurrent(inp2)
inp3 = [7,7,7,7]
smallerNumbersThanCurrent(inp3)
