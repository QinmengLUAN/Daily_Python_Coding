"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.

Here's a start:

def products(nums):
  # Fill this in.

print products([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]

"""
def products(nums):
    total = 1
    for num in nums:
        total *= num
    res = []
    for num in nums:
        res.append(total//num)
    return res

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]