"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.

def findPythagoreanTriplets(nums):
  # Fill this in.

print findPythagoreanTriplets([3, 12, 5, 13])
# True
"""
def findPythagoreanTriplets(nums):
  # Fill this in.
  nums.sort()
  for i in range(len(nums)):
    nums[i] *= nums[i]
  nums_set = set(nums)
  print(nums_set)
  for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] in nums_set:
            return True
  return False

def findPythagoreanTriplets2(nums):
    nums.sort()
    b = c = 0

    for val in nums:
        # odd number
        if val % 2 != 0:
            b = val**2 // 2
            c = b + 1
            if b in nums and c in nums:
                return True
        # even number
        else:
            b = (val // 2)**2 - 1
            c = b + 2
            if b in nums and c in nums:
                return True
    return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True