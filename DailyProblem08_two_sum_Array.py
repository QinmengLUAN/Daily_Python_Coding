"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5, 
return true since 4 + 1 = 5.

def two_sum(list, k):
  # Fill this in.

print two_sum([4,7,1,-3,2], 5)
# True

Try to do it in a single pass of the list.
"""
def two_sum(nums, k):
  # Fill this in.
  res_set = set()
  for n in nums:
    if n in res_set:
        return True
    else:
        res_set.add(k-n)
  return False

print(two_sum([4,7,1,-3,2], 5))
# True